#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
规则集获取模块

负责从blackmatrix7/ios_rule_script仓库获取各种分流规则集，
包括流媒体、社交媒体、AI服务、科技巨头、游戏服务、金融服务、
购物电商、新闻媒体、开发工具和广告拦截等规则集。
"""

import requests
import os
import time
import json
from config import RULESET_URLS, REQUEST_TIMEOUT, USER_AGENT, GROUP_TYPE_MAPPING

# 缓存配置
CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cache')
CACHE_EXPIRY = 3600 * 24  # 缓存24小时

# 全局缓存
_cache = {}

def load_cache():
    """加载缓存"""
    global _cache
    cache_file = os.path.join(CACHE_DIR, 'rulesets_cache.json')
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                _cache = json.load(f)
        except Exception as e:
            print(f"加载缓存失败: {str(e)}")
            _cache = {}

def save_cache():
    """保存缓存"""
    global _cache
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_file = os.path.join(CACHE_DIR, 'rulesets_cache.json')
    try:
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(_cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存缓存失败: {str(e)}")

def is_cache_valid(cache_key):
    """检查缓存是否有效"""
    global _cache
    if cache_key not in _cache:
        return False
    
    cache_time = _cache[cache_key].get('timestamp', 0)
    return time.time() - cache_time < CACHE_EXPIRY

def get_from_cache(cache_key):
    """从缓存获取数据"""
    global _cache
    if is_cache_valid(cache_key):
        return _cache[cache_key].get('data')
    return None

def set_cache(cache_key, data):
    """设置缓存"""
    global _cache
    _cache[cache_key] = {
        'data': data,
        'timestamp': time.time()
    }

def fetch_ruleset(ruleset_name, url):
    """
    获取单个规则集
    
    Args:
        ruleset_name (str): 规则集名称
        url (str): 规则集URL
        
    Returns:
        list: 规则列表，获取失败返回空列表
    """
    cache_key = f"ruleset_{ruleset_name}"
    
    # 尝试从缓存获取
    cached_data = get_from_cache(cache_key)
    if cached_data is not None:
        print(f"从缓存获取规则集: {ruleset_name}")
        return cached_data
    
    print(f"正在获取规则集: {ruleset_name}")
    
    try:
        headers = {
            'User-Agent': USER_AGENT,
            'Accept': 'text/plain, application/yaml, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        # 解析YAML内容，提取规则
        content = response.text.strip()
        rules = []
        
        # 处理YAML格式的规则集
        lines = content.split('\n')
        in_payload = False
        
        for line in lines:
            line = line.strip()
            
            # 跳过注释和空行
            if not line or line.startswith('#'):
                continue
            
            # 检查是否进入payload部分
            if line.startswith('payload:'):
                in_payload = True
                continue
            
            # 如果在payload部分，提取规则
            if in_payload:
                # 移除YAML列表标记
                if line.startswith('- '):
                    rule = line[2:].strip()
                    # 移除引号
                    if rule.startswith('"') and rule.endswith('"'):
                        rule = rule[1:-1]
                    elif rule.startswith("'") and rule.endswith("'"):
                        rule = rule[1:-1]
                    
                    if rule:
                        rules.append(rule)
                elif line and not line.startswith(' '):
                    # 如果遇到非缩进行，说明payload部分结束
                    break
        
        # 如果没有找到payload部分，尝试直接解析规则
        if not rules:
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('payload:'):
                    # 检查是否是有效的规则格式
                    if any(line.startswith(prefix) for prefix in ['DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD', 'IP-CIDR', 'GEOIP', 'PROCESS-NAME', 'URL-REGEX']):
                        rules.append(line)
        
        print(f"成功获取规则集 {ruleset_name}，包含 {len(rules)} 条规则")
        
        # 缓存结果
        set_cache(cache_key, rules)
        
        return rules
        
    except requests.exceptions.RequestException as e:
        print(f"获取规则集 {ruleset_name} 失败: {str(e)}")
        return []
    except Exception as e:
        print(f"解析规则集 {ruleset_name} 失败: {str(e)}")
        return []

def get_rulesets_for_groups(group_types):
    """
    根据策略组类型获取对应的规则集
    
    Args:
        group_types (list): 策略组类型列表
        
    Returns:
        dict: 规则集字典，键为规则集名称，值为规则列表
    """
    rulesets = {}
    
    for group_type in group_types:
        if group_type in GROUP_TYPE_MAPPING:
            rules = GROUP_TYPE_MAPPING[group_type]
            for rule in rules:
                # 解析规则格式: RULE-SET,ruleset_name,policy_name
                parts = rule.split(',')
                if len(parts) >= 2 and parts[0] == 'RULE-SET':
                    ruleset_name = parts[1]
                    if ruleset_name in RULESET_URLS:
                        url = RULESET_URLS[ruleset_name]
                        ruleset_data = fetch_ruleset(ruleset_name, url)
                        if ruleset_data:
                            rulesets[ruleset_name] = ruleset_data
    
    return rulesets

def get_all_rulesets():
    """
    获取所有可用的规则集
    
    Returns:
        dict: 规则集字典，键为规则集名称，值为规则列表
    """
    rulesets = {}
    
    for ruleset_name, url in RULESET_URLS.items():
        ruleset_data = fetch_ruleset(ruleset_name, url)
        if ruleset_data:
            rulesets[ruleset_name] = ruleset_data
    
    return rulesets

def get_streaming_rulesets():
    """
    获取流媒体相关的规则集
    
    Returns:
        dict: 流媒体规则集字典
    """
    return get_rulesets_for_groups(['streaming'])

def get_social_rulesets():
    """
    获取社交媒体相关的规则集
    
    Returns:
        dict: 社交媒体规则集字典
    """
    return get_rulesets_for_groups(['social'])

def get_ai_rulesets():
    """
    获取AI服务相关的规则集
    
    Returns:
        dict: AI服务规则集字典
    """
    return get_rulesets_for_groups(['ai'])

def get_techgiants_rulesets():
    """
    获取科技巨头相关的规则集
    
    Returns:
        dict: 科技巨头规则集字典
    """
    return get_rulesets_for_groups(['techgiants'])

def get_gaming_rulesets():
    """
    获取游戏服务相关的规则集
    
    Returns:
        dict: 游戏服务规则集字典
    """
    return get_rulesets_for_groups(['gaming'])

def get_finance_rulesets():
    """
    获取金融服务相关的规则集
    
    Returns:
        dict: 金融服务规则集字典
    """
    return get_rulesets_for_groups(['finance'])

def get_shopping_rulesets():
    """
    获取购物电商相关的规则集
    
    Returns:
        dict: 购物电商规则集字典
    """
    return get_rulesets_for_groups(['shopping'])

def get_news_rulesets():
    """
    获取新闻媒体相关的规则集
    
    Returns:
        dict: 新闻媒体规则集字典
    """
    return get_rulesets_for_groups(['news'])

def get_developer_rulesets():
    """
    获取开发工具相关的规则集
    
    Returns:
        dict: 开发工具规则集字典
    """
    return get_rulesets_for_groups(['developer'])

def get_adblock_rulesets():
    """
    获取广告拦截相关的规则集
    
    Returns:
        dict: 广告拦截规则集字典
    """
    return get_rulesets_for_groups(['adblock'])

def generate_rules_for_groups(group_types):
    """
    根据策略组类型生成对应的规则列表
    
    Args:
        group_types (list): 策略组类型列表
        
    Returns:
        list: 规则列表
    """
    rules = []
    
    for group_type in group_types:
        if group_type in GROUP_TYPE_MAPPING:
            group_rules = GROUP_TYPE_MAPPING[group_type]
            rules.extend(group_rules)
    
    return rules

def get_available_rulesets():
    """
    获取所有可用的规则集名称列表
    
    Returns:
        list: 规则集名称列表
    """
    return list(RULESET_URLS.keys())

def validate_ruleset_url(url):
    """
    验证规则集URL是否可访问
    
    Args:
        url (str): 规则集URL
        
    Returns:
        bool: URL是否可访问
    """
    try:
        headers = {'User-Agent': USER_AGENT}
        response = requests.head(url, headers=headers, timeout=10)
        return response.status_code == 200
    except:
        return False

def get_ruleset_info():
    """
    获取规则集信息
    
    Returns:
        dict: 规则集信息字典
    """
    info = {
        'total_rulesets': len(RULESET_URLS),
        'categories': {
            'streaming': len([r for r in GROUP_TYPE_MAPPING.get('streaming', [])]),
            'social': len([r for r in GROUP_TYPE_MAPPING.get('social', [])]),
            'ai': len([r for r in GROUP_TYPE_MAPPING.get('ai', [])]),
            'techgiants': len([r for r in GROUP_TYPE_MAPPING.get('techgiants', [])]),
            'gaming': len([r for r in GROUP_TYPE_MAPPING.get('gaming', [])]),
            'finance': len([r for r in GROUP_TYPE_MAPPING.get('finance', [])]),
            'shopping': len([r for r in GROUP_TYPE_MAPPING.get('shopping', [])]),
            'news': len([r for r in GROUP_TYPE_MAPPING.get('news', [])]),
            'developer': len([r for r in GROUP_TYPE_MAPPING.get('developer', [])]),
            'adblock': len([r for r in GROUP_TYPE_MAPPING.get('adblock', [])]),
        },
        'source': 'blackmatrix7/ios_rule_script',
        'cache_expiry_hours': CACHE_EXPIRY // 3600
    }
    
    return info

