#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置生成模块

负责整合节点、策略组和规则，生成最终的Clash配置文件。
"""

import json
import os

def generate_clash_config(proxies, proxy_groups, rules, rulesets):
    """
    生成Clash配置文件
    
    Args:
        proxies: 代理节点列表
        proxy_groups: 策略组列表
        rules: 规则列表
        rulesets: 规则集字典
        
    Returns:
        str: YAML格式的Clash配置文件内容
    """
    
    # 基础配置
    config = {
        'port': 7890,
        'socks-port': 7891,
        'allow-lan': True,
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
    
    # 添加代理节点
    config['proxies'] = proxies
    
    # 添加策略组
    config['proxy-groups'] = proxy_groups
    
    # 添加规则集
    if rulesets:
        config['rule-providers'] = {}
        for name, content in rulesets.items():
            config['rule-providers'][name] = {
                'type': 'http',
                'behavior': 'domain',
                'url': f"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/{name.title()}/{name.title()}.yaml",
                'path': f"./ruleset/{name}.yaml",
                'interval': 86400
            }
    
    # 添加规则
    config['rules'] = rules
    
    # 转换为YAML格式（手动实现）
    yaml_content = convert_dict_to_yaml(config)
    
    return yaml_content

def convert_dict_to_yaml(data, indent=0):
    """手动将字典转换为YAML格式"""
    yaml_lines = []
    indent_str = '  ' * indent
    
    for key, value in data.items():
        if isinstance(value, dict):
            yaml_lines.append(f"{indent_str}{key}:")
            yaml_lines.append(convert_dict_to_yaml(value, indent + 1))
        elif isinstance(value, list):
            yaml_lines.append(f"{indent_str}{key}:")
            for item in value:
                if isinstance(item, dict):
                    yaml_lines.append(f"{indent_str}  -")
                    for sub_key, sub_value in item.items():
                        if isinstance(sub_value, (str, int, bool)):
                            yaml_lines.append(f"{indent_str}    {sub_key}: {sub_value}")
                        elif isinstance(sub_value, list):
                            yaml_lines.append(f"{indent_str}    {sub_key}:")
                            for sub_item in sub_value:
                                yaml_lines.append(f"{indent_str}      - {sub_item}")
                else:
                    yaml_lines.append(f"{indent_str}  - {item}")
        else:
            yaml_lines.append(f"{indent_str}{key}: {value}")
    
    return '\n'.join(yaml_lines)

