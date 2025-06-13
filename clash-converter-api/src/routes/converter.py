from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import sys
import os
import tempfile
import traceback
from datetime import datetime

# 添加模块路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ..modules.subscription import fetch_subscription, parse_subscription
from ..modules.proxy_groups import generate_all_groups
from ..modules.rulesets import get_rulesets_for_groups, generate_rules_for_groups
from ..modules.generator import generate_clash_config
from ..config import GROUP_TYPES

converter_bp = Blueprint('converter', __name__)

@converter_bp.route('/convert', methods=['POST', 'OPTIONS'])
@cross_origin()
def convert_subscription():
    """转换订阅链接为Clash配置"""
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        
        # 验证输入参数
        if not data or 'subscription_url' not in data:
            return jsonify({
                'success': False,
                'error': '缺少订阅链接参数'
            }), 400
        
        subscription_url = data['subscription_url']
        selected_groups = data.get('selected_groups', ['streaming', 'social', 'ai', 'adblock'])
        output_filename = data.get('output_filename', 'clash_config.yaml')
        
        # 步骤1: 获取订阅内容
        subscription_content = fetch_subscription(subscription_url)
        if not subscription_content:
            return jsonify({
                'success': False,
                'error': '无法获取订阅内容'
            }), 400
        
        # 步骤2: 解析订阅内容
        proxies = parse_subscription(subscription_content)
        if not proxies:
            return jsonify({
                'success': False,
                'error': '无法解析订阅内容或订阅中没有有效节点'
            }), 400
        
        # 获取代理节点名称列表
        proxy_names = [proxy['name'] for proxy in proxies]
        
        # 步骤3: 生成策略组
        proxy_groups = generate_all_groups(proxy_names, selected_groups)
        
        # 步骤4: 获取规则集和生成规则
        rulesets = get_rulesets_for_groups(selected_groups)
        rules = generate_rules_for_groups(selected_groups)
        
        # 步骤5: 生成配置文件
        config_content = generate_clash_config(
            proxies, proxy_groups, rules, rulesets
        )
        
        # 统计信息
        stats = {
            'proxies': len(proxies),
            'groups': len(proxy_groups),
            'rules': len(rules),
            'rulesets': len(rulesets)
        }
        
        # 获取选中的策略组名称
        selected_group_names = []
        for group_id in selected_groups:
            if group_id in GROUP_TYPES:
                selected_group_names.append(GROUP_TYPES[group_id]['name'])
        
        return jsonify({
            'success': True,
            'message': '转换完成！',
            'stats': stats,
            'selected_groups': selected_group_names,
            'config_content': config_content,
            'filename': output_filename,
            'generated_at': datetime.now().isoformat()
        })
        
    except Exception as e:
        error_msg = f"转换失败: {str(e)}"
        print(f"Error: {error_msg}")
        print(traceback.format_exc())
        return jsonify({
            'success': False,
            'error': error_msg
        }), 500

@converter_bp.route('/info', methods=['GET'])
@cross_origin()
def get_info():
    """获取程序信息"""
    try:
        # 统计规则集信息
        total_rulesets = 76  # 预设值
        
        return jsonify({
            'success': True,
            'info': {
                'version': 'v2.0',
                'total_rulesets': total_rulesets,
                'group_types': len(GROUP_TYPES),
                'rule_source': 'blackmatrix7/ios_rule_script',
                'features': [
                    '支持多种订阅格式',
                    '智能缓存系统',
                    '精细分流规则',
                    '完善错误处理',
                    '响应式Web界面'
                ]
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@converter_bp.route('/groups', methods=['GET'])
@cross_origin()
def get_groups():
    """获取策略组类型列表"""
    try:
        return jsonify({
            'success': True,
            'groups': GROUP_TYPES
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@converter_bp.route('/health', methods=['GET'])
@cross_origin()
def health_check():
    """健康检查"""
    return jsonify({
        'success': True,
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

