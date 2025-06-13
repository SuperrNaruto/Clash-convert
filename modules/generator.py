#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置生成模块

负责整合节点、策略组和规则，生成最终的Clash配置文件。
支持多种策略组类型和从blackmatrix7仓库获取的规则集。
"""

import yaml
import os
from config import TEMPLATE_CONFIG, BASE_RULES

def load_base_config():
    """
    加载基础配置模板
    
    Returns:
        dict: 基础配置字典
    """
    if os.path.exists(TEMPLATE_CONFIG):
        try:
            with open(TEMPLATE_CONFIG, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"加载基础配置模板失败: {str(e)}")
    
    # 如果模板文件不存在，返回默认配置
    return {
        'port': 7890,
        'socks-port': 7891,
        'allow-lan': False,
        'mode': 'rule',
        'log-level': 'info',
        'external-controller': '127.0.0.1:9090',
        'dns': {
            'enable': True,
            'ipv6': False,
            'default-nameserver': ['223.5.5.5', '119.29.29.29'],
            'enhanced-mode': 'fake-ip',
            'fake-ip-range': '198.18.0.1/16',
            'use-hosts': True,
            'nameserver': ['https://doh.pub/dns-query', 'https://dns.alidns.com/dns-query'],
            'fallback': ['https://doh.dns.sb/dns-query', 'https://dns.cloudflare.com/dns-query', 'https://dns.twnic.tw/dns-query', 'tls://8.8.4.4:853'],
            'fallback-filter': {
                'geoip': True,
                'ipcidr': ['240.0.0.0/4', '0.0.0.0/32']
            }
        }
    }

def format_rules_with_rulesets(rules, rulesets):
    """
    格式化规则，将RULE-SET规则转换为实际规则
    
    Args:
        rules (list): 规则列表
        rulesets (dict): 规则集字典
        
    Returns:
        list: 格式化后的规则列表
    """
    formatted_rules = []
    
    for rule in rules:
        if rule.startswith('RULE-SET,'):
            # 解析RULE-SET规则: RULE-SET,ruleset_name,policy_name
            parts = rule.split(',')
            if len(parts) >= 3:
                ruleset_name = parts[1]
                policy_name = parts[2]
                
                # 如果规则集存在，添加其中的规则
                if ruleset_name in rulesets:
                    ruleset_rules = rulesets[ruleset_name]
                    for ruleset_rule in ruleset_rules:
                        # 为每条规则添加策略名称
                        if ',' in ruleset_rule:
                            # 如果规则已经包含策略，替换为新策略
                            rule_parts = ruleset_rule.split(',')
                            if len(rule_parts) >= 2:
                                formatted_rule = f"{rule_parts[0]},{rule_parts[1]},{policy_name}"
                                formatted_rules.append(formatted_rule)
                        else:
                            # 如果规则不包含策略，添加策略
                            formatted_rule = f"{ruleset_rule},{policy_name}"
                            formatted_rules.append(formatted_rule)
                else:
                    print(f"警告: 规则集 {ruleset_name} 不存在，跳过相关规则")
        else:
            # 非RULE-SET规则直接添加
            formatted_rules.append(rule)
    
    return formatted_rules

def generate_clash_config(proxies, proxy_groups, rules, rulesets=None):
    """
    生成完整的Clash配置文件
    
    Args:
        proxies (list): 代理节点列表
        proxy_groups (list): 策略组列表
        rules (list): 规则列表
        rulesets (dict): 规则集字典，可选
        
    Returns:
        str: YAML格式的配置文件内容
    """
    # 加载基础配置
    config = load_base_config()
    
    # 添加代理节点
    config['proxies'] = proxies
    
    # 添加策略组
    config['proxy-groups'] = proxy_groups
    
    # 处理规则
    if rulesets:
        # 如果提供了规则集，将RULE-SET规则展开
        formatted_rules = format_rules_with_rulesets(rules, rulesets)
    else:
        formatted_rules = rules
    
    # 添加基础规则
    all_rules = formatted_rules + BASE_RULES
    config['rules'] = all_rules
    
    # 转换为YAML格式
    try:
        yaml_content = yaml.dump(config, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return yaml_content
    except Exception as e:
        print(f"生成YAML配置失败: {str(e)}")
        return ""

def generate_config_with_custom_rules(proxies, proxy_groups, custom_rules):
    """
    使用自定义规则生成配置文件
    
    Args:
        proxies (list): 代理节点列表
        proxy_groups (list): 策略组列表
        custom_rules (list): 自定义规则列表
        
    Returns:
        str: YAML格式的配置文件内容
    """
    return generate_clash_config(proxies, proxy_groups, custom_rules)

def validate_config(config_content):
    """
    验证配置文件格式是否正确
    
    Args:
        config_content (str): 配置文件内容
        
    Returns:
        tuple: (是否有效, 错误信息)
    """
    try:
        config = yaml.safe_load(config_content)
        
        # 检查必要字段
        required_fields = ['proxies', 'proxy-groups', 'rules']
        for field in required_fields:
            if field not in config:
                return False, f"缺少必要字段: {field}"
        
        # 检查代理节点格式
        if not isinstance(config['proxies'], list):
            return False, "proxies字段必须是列表"
        
        # 检查策略组格式
        if not isinstance(config['proxy-groups'], list):
            return False, "proxy-groups字段必须是列表"
        
        # 检查规则格式
        if not isinstance(config['rules'], list):
            return False, "rules字段必须是列表"
        
        return True, "配置文件格式正确"
        
    except yaml.YAMLError as e:
        return False, f"YAML格式错误: {str(e)}"
    except Exception as e:
        return False, f"验证失败: {str(e)}"

def save_config_to_file(config_content, file_path):
    """
    保存配置文件到指定路径
    
    Args:
        config_content (str): 配置文件内容
        file_path (str): 文件路径
        
    Returns:
        bool: 是否保存成功
    """
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(config_content)
        
        return True
    except Exception as e:
        print(f"保存配置文件失败: {str(e)}")
        return False

def get_config_stats(config_content):
    """
    获取配置文件统计信息
    
    Args:
        config_content (str): 配置文件内容
        
    Returns:
        dict: 统计信息字典
    """
    try:
        config = yaml.safe_load(config_content)
        
        stats = {
            'proxies_count': len(config.get('proxies', [])),
            'proxy_groups_count': len(config.get('proxy-groups', [])),
            'rules_count': len(config.get('rules', [])),
            'dns_enabled': config.get('dns', {}).get('enable', False),
            'mode': config.get('mode', 'unknown'),
            'port': config.get('port', 0),
            'socks_port': config.get('socks-port', 0)
        }
        
        return stats
    except Exception as e:
        print(f"获取配置统计信息失败: {str(e)}")
        return {}

def merge_configs(base_config, additional_config):
    """
    合并两个配置文件
    
    Args:
        base_config (str): 基础配置文件内容
        additional_config (str): 附加配置文件内容
        
    Returns:
        str: 合并后的配置文件内容
    """
    try:
        base = yaml.safe_load(base_config)
        additional = yaml.safe_load(additional_config)
        
        # 合并代理节点
        if 'proxies' in additional:
            base.setdefault('proxies', []).extend(additional['proxies'])
        
        # 合并策略组
        if 'proxy-groups' in additional:
            base.setdefault('proxy-groups', []).extend(additional['proxy-groups'])
        
        # 合并规则（附加规则插入到基础规则之前）
        if 'rules' in additional:
            base_rules = base.get('rules', [])
            additional_rules = additional['rules']
            base['rules'] = additional_rules + base_rules
        
        # 合并其他配置（附加配置优先）
        for key, value in additional.items():
            if key not in ['proxies', 'proxy-groups', 'rules']:
                base[key] = value
        
        return yaml.dump(base, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
    except Exception as e:
        print(f"合并配置文件失败: {str(e)}")
        return base_config

