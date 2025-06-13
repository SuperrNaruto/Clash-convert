#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
规则集获取模块

负责从blackmatrix7/ios_rule_script仓库获取各种分流规则集。
"""

import requests
import os
import time
import json

# 配置常量
REQUEST_TIMEOUT = 30
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# blackmatrix7 规则集URL配置
BLACKMATRIX7_BASE_URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash"

# 规则集URL映射
RULESET_URLS = {
    'streaming': {
        'netflix': f"{BLACKMATRIX7_BASE_URL}/Netflix/Netflix.yaml",
        'youtube': f"{BLACKMATRIX7_BASE_URL}/YouTube/YouTube.yaml",
        'spotify': f"{BLACKMATRIX7_BASE_URL}/Spotify/Spotify.yaml",
    },
    'social': {
        'telegram': f"{BLACKMATRIX7_BASE_URL}/Telegram/Telegram.yaml",
        'twitter': f"{BLACKMATRIX7_BASE_URL}/Twitter/Twitter.yaml",
        'facebook': f"{BLACKMATRIX7_BASE_URL}/Facebook/Facebook.yaml",
    },
    'ai': {
        'openai': f"{BLACKMATRIX7_BASE_URL}/OpenAI/OpenAI.yaml",
        'anthropic': f"{BLACKMATRIX7_BASE_URL}/Anthropic/Anthropic.yaml",
    },
    'techgiants': {
        'apple': f"{BLACKMATRIX7_BASE_URL}/Apple/Apple.yaml",
        'google': f"{BLACKMATRIX7_BASE_URL}/Google/Google.yaml",
        'microsoft': f"{BLACKMATRIX7_BASE_URL}/Microsoft/Microsoft.yaml",
    },
    'gaming': {
        'steam': f"{BLACKMATRIX7_BASE_URL}/Steam/Steam.yaml",
        'epicgames': f"{BLACKMATRIX7_BASE_URL}/Epic/Epic.yaml",
    },
    'finance': {
        'paypal': f"{BLACKMATRIX7_BASE_URL}/PayPal/PayPal.yaml",
    },
    'shopping': {
        'amazon': f"{BLACKMATRIX7_BASE_URL}/Amazon/Amazon.yaml",
        'taobao': f"{BLACKMATRIX7_BASE_URL}/Taobao/Taobao.yaml",
    },
    'news': {
        'bbc': f"{BLACKMATRIX7_BASE_URL}/BBC/BBC.yaml",
        'cnn': f"{BLACKMATRIX7_BASE_URL}/CNN/CNN.yaml",
    },
    'developer': {
        'github': f"{BLACKMATRIX7_BASE_URL}/GitHub/GitHub.yaml",
        'stackoverflow': f"{BLACKMATRIX7_BASE_URL}/StackOverflow/StackOverflow.yaml",
    },
    'adblock': {
        'advertising': f"{BLACKMATRIX7_BASE_URL}/Advertising/Advertising.yaml",
        'privacy': f"{BLACKMATRIX7_BASE_URL}/Privacy/Privacy.yaml",
    }
}

# 缓存配置
CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cache')
CACHE_EXPIRY = 3600 * 24  # 缓存24小时

def ensure_cache_dir():
    """确保缓存目录存在"""
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

def get_cache_path(ruleset_name):
    """获取规则集缓存文件路径"""
    return os.path.join(CACHE_DIR, f"{ruleset_name}.yaml")

def is_cache_valid(cache_path):
    """检查缓存是否有效"""
    if not os.path.exists(cache_path):
        return False
    
    # 检查缓存时间
    cache_time = os.path.getmtime(cache_path)
    current_time = time.time()
    return (current_time - cache_time) < CACHE_EXPIRY

def fetch_ruleset(url, ruleset_name):
    """
    获取规则集内容
    
    Args:
        url: 规则集URL
        ruleset_name: 规则集名称
        
    Returns:
        str: 规则集内容
    """
    ensure_cache_dir()
    cache_path = get_cache_path(ruleset_name)
    
    # 检查缓存
    if is_cache_valid(cache_path):
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"读取缓存失败: {str(e)}")
    
    # 从网络获取
    try:
        headers = {'User-Agent': USER_AGENT}
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        content = response.text
        
        # 保存到缓存
        try:
            with open(cache_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"保存缓存失败: {str(e)}")
        
        return content
    except Exception as e:
        print(f"获取规则集失败 {ruleset_name}: {str(e)}")
        return None

def get_rulesets_for_groups(group_types):
    """
    获取指定策略组类型的规则集
    
    Args:
        group_types: 策略组类型列表
        
    Returns:
        dict: 规则集内容字典
    """
    rulesets = {}
    
    for group_type in group_types:
        if group_type in RULESET_URLS:
            for ruleset_name, url in RULESET_URLS[group_type].items():
                content = fetch_ruleset(url, ruleset_name)
                if content:
                    rulesets[ruleset_name] = content
    
    return rulesets

def generate_rules_for_groups(group_types):
    """
    生成指定策略组类型的规则
    
    Args:
        group_types: 策略组类型列表
        
    Returns:
        list: 规则列表
    """
    rules = []
    
    # 基础规则
    base_rules = [
        'RULE-SET,applications,DIRECT',
        'DOMAIN,clash.razord.top,DIRECT',
        'DOMAIN,yacd.haishan.me,DIRECT',
        'RULE-SET,private,DIRECT',
        'GEOIP,LAN,DIRECT',
        'GEOIP,CN,DIRECT',
        'MATCH,🐟 漏网之鱼'
    ]
    
    # 策略组规则映射
    group_rules = {
        'streaming': [
            'RULE-SET,netflix,🎬 流媒体服务',
            'RULE-SET,youtube,🎬 流媒体服务',
            'RULE-SET,spotify,🎬 流媒体服务',
        ],
        'social': [
            'RULE-SET,telegram,💬 社交媒体',
            'RULE-SET,twitter,💬 社交媒体',
            'RULE-SET,facebook,💬 社交媒体',
        ],
        'ai': [
            'RULE-SET,openai,🤖 AI服务',
            'RULE-SET,anthropic,🤖 AI服务',
        ],
        'techgiants': [
            'RULE-SET,apple,🏢 科技巨头',
            'RULE-SET,google,🏢 科技巨头',
            'RULE-SET,microsoft,🏢 科技巨头',
        ],
        'gaming': [
            'RULE-SET,steam,🎮 游戏服务',
            'RULE-SET,epicgames,🎮 游戏服务',
        ],
        'finance': [
            'RULE-SET,paypal,💰 金融服务',
        ],
        'shopping': [
            'RULE-SET,amazon,🛒 购物电商',
            'RULE-SET,taobao,🛒 购物电商',
        ],
        'news': [
            'RULE-SET,bbc,📰 新闻媒体',
            'RULE-SET,cnn,📰 新闻媒体',
        ],
        'developer': [
            'RULE-SET,github,💻 开发工具',
            'RULE-SET,stackoverflow,💻 开发工具',
        ],
        'adblock': [
            'RULE-SET,advertising,🛡️ 广告拦截',
            'RULE-SET,privacy,🛡️ 广告拦截',
        ]
    }
    
    # 添加广告拦截规则（如果包含）
    if 'adblock' in group_types:
        rules.extend(group_rules['adblock'])
    
    # 添加其他策略组规则
    for group_type in group_types:
        if group_type in group_rules and group_type != 'adblock':
            rules.extend(group_rules[group_type])
    
    # 添加基础规则
    rules.extend(base_rules)
    
    return rules

