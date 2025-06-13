#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
策略组生成模块

负责生成各种类型的策略组配置，包括流媒体、社交媒体、AI服务、科技巨头、
游戏服务、金融服务、购物电商、新闻媒体、开发工具和广告拦截等。
"""

import yaml
import os
from config import TEMPLATE_GROUPS

def load_template_groups(group_type):
    """
    加载策略组模板
    
    Args:
        group_type (str): 策略组类型
        
    Returns:
        list: 策略组配置列表
    """
    template_path = TEMPLATE_GROUPS.get(group_type)
    if not template_path or not os.path.exists(template_path):
        print(f"警告: 策略组模板文件不存在: {template_path}")
        return []
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # 移除注释行
            lines = [line for line in content.split('\n') if not line.strip().startswith('#')]
            content = '\n'.join(lines)
            groups = yaml.safe_load(content)
            return groups if groups else []
    except Exception as e:
        print(f"加载策略组模板失败: {str(e)}")
        return []

def generate_basic_groups(proxy_names):
    """
    生成基础策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 基础策略组配置列表
    """
    basic_groups = [
        {
            'name': '🚀 节点选择',
            'type': 'select',
            'proxies': ['♻️ 自动选择', '🔯 故障转移', '🔮 负载均衡'] + proxy_names
        },
        {
            'name': '♻️ 自动选择',
            'type': 'url-test',
            'proxies': proxy_names,
            'url': 'http://www.gstatic.com/generate_204',
            'interval': 300
        },
        {
            'name': '🔯 故障转移',
            'type': 'fallback',
            'proxies': proxy_names,
            'url': 'http://www.gstatic.com/generate_204',
            'interval': 300
        },
        {
            'name': '🔮 负载均衡',
            'type': 'load-balance',
            'strategy': 'consistent-hashing',
            'proxies': proxy_names,
            'url': 'http://www.gstatic.com/generate_204',
            'interval': 300
        },
        {
            'name': '🐟 漏网之鱼',
            'type': 'select',
            'proxies': ['🚀 节点选择', 'DIRECT']
        }
    ]
    
    return basic_groups

def generate_streaming_groups(proxy_names):
    """
    生成流媒体策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 流媒体策略组配置列表
    """
    groups = load_template_groups('streaming')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            # 在现有选项后添加代理节点
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_social_groups(proxy_names):
    """
    生成社交媒体策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 社交媒体策略组配置列表
    """
    groups = load_template_groups('social')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_ai_groups(proxy_names):
    """
    生成AI服务策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: AI服务策略组配置列表
    """
    groups = load_template_groups('ai')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_techgiants_groups(proxy_names):
    """
    生成科技巨头策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 科技巨头策略组配置列表
    """
    groups = load_template_groups('techgiants')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_gaming_groups(proxy_names):
    """
    生成游戏服务策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 游戏服务策略组配置列表
    """
    groups = load_template_groups('gaming')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_finance_groups(proxy_names):
    """
    生成金融服务策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 金融服务策略组配置列表
    """
    groups = load_template_groups('finance')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_shopping_groups(proxy_names):
    """
    生成购物电商策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 购物电商策略组配置列表
    """
    groups = load_template_groups('shopping')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_news_groups(proxy_names):
    """
    生成新闻媒体策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 新闻媒体策略组配置列表
    """
    groups = load_template_groups('news')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_developer_groups(proxy_names):
    """
    生成开发工具策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 开发工具策略组配置列表
    """
    groups = load_template_groups('developer')
    
    # 为每个策略组添加代理节点选项
    for group in groups:
        if 'proxies' in group:
            group['proxies'].extend(proxy_names)
    
    return groups

def generate_adblock_groups(proxy_names):
    """
    生成广告拦截策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        
    Returns:
        list: 广告拦截策略组配置列表
    """
    groups = load_template_groups('adblock')
    
    # 广告拦截组不需要添加代理节点，因为它们主要使用REJECT和DIRECT
    return groups

def generate_all_groups(proxy_names, include_types=None):
    """
    生成所有策略组
    
    Args:
        proxy_names (list): 代理节点名称列表
        include_types (list): 要包含的策略组类型列表，None表示包含所有类型
        
    Returns:
        list: 所有策略组配置列表
    """
    all_groups = []
    
    # 基础策略组（始终包含）
    all_groups.extend(generate_basic_groups(proxy_names))
    
    # 可选策略组
    group_generators = {
        'streaming': generate_streaming_groups,
        'social': generate_social_groups,
        'ai': generate_ai_groups,
        'techgiants': generate_techgiants_groups,
        'gaming': generate_gaming_groups,
        'finance': generate_finance_groups,
        'shopping': generate_shopping_groups,
        'news': generate_news_groups,
        'developer': generate_developer_groups,
        'adblock': generate_adblock_groups,
    }
    
    # 如果没有指定类型，包含所有类型
    if include_types is None:
        include_types = list(group_generators.keys())
    
    # 生成指定类型的策略组
    for group_type in include_types:
        if group_type in group_generators:
            groups = group_generators[group_type](proxy_names)
            all_groups.extend(groups)
        else:
            print(f"警告: 未知的策略组类型: {group_type}")
    
    return all_groups

def get_available_group_types():
    """
    获取可用的策略组类型列表
    
    Returns:
        list: 可用的策略组类型列表
    """
    return [
        'streaming',    # 流媒体服务
        'social',       # 社交媒体
        'ai',           # AI服务
        'techgiants',   # 科技巨头
        'gaming',       # 游戏服务
        'finance',      # 金融服务
        'shopping',     # 购物电商
        'news',         # 新闻媒体
        'developer',    # 开发工具
        'adblock',      # 广告拦截
    ]

