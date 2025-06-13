#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
规则集获取功能测试脚本
"""

import sys
import os
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.rulesets import fetch_rulesets, get_adblock_rules, fetch_ruleset_files

def test_rulesets():
    """测试规则集获取功能"""
    print("测试规则集获取功能...")
    
    # 测试获取基础规则集
    print("\n测试获取基础规则集...")
    rulesets = fetch_rulesets([])
    print(f"获取到 {len(rulesets)} 条规则")
    for i, rule in enumerate(rulesets[:5]):
        print(f"规则 {i+1}: {rule}")
    if len(rulesets) > 5:
        print(f"... 还有 {len(rulesets) - 5} 条规则")
    
    # 测试获取流媒体规则集
    print("\n测试获取流媒体规则集...")
    # 先获取规则集文件
    print("获取流媒体规则集文件...")
    fetch_ruleset_files(['youtube', 'netflix', 'disney', 'spotify', 'bilibili'])
    # 获取规则集
    rulesets = fetch_rulesets(['streaming'])
    print(f"获取到 {len(rulesets)} 条规则")
    # 过滤出流媒体规则
    streaming_rules = [rule for rule in rulesets if any(media in rule for media in ['YouTube', 'Netflix', 'Disney+', 'Spotify', '哔哩哔哩'])]
    for i, rule in enumerate(streaming_rules):
        print(f"流媒体规则 {i+1}: {rule}")
    
    # 测试获取社交媒体规则集
    print("\n测试获取社交媒体规则集...")
    # 先获取规则集文件
    print("获取社交媒体规则集文件...")
    fetch_ruleset_files(['telegram', 'twitter', 'instagram', 'facebook'])
    # 获取规则集
    rulesets = fetch_rulesets(['social'])
    print(f"获取到 {len(rulesets)} 条规则")
    # 过滤出社交媒体规则
    social_rules = [rule for rule in rulesets if any(social in rule for social in ['Telegram', 'Twitter', 'Instagram', 'Facebook'])]
    for i, rule in enumerate(social_rules):
        print(f"社交媒体规则 {i+1}: {rule}")
    
    # 测试获取AI服务规则集
    print("\n测试获取AI服务规则集...")
    # 先获取规则集文件
    print("获取AI服务规则集文件...")
    fetch_ruleset_files(['openai', 'claude'])
    # 获取规则集
    rulesets = fetch_rulesets(['ai'])
    print(f"获取到 {len(rulesets)} 条规则")
    # 过滤出AI服务规则
    ai_rules = [rule for rule in rulesets if any(ai in rule for ai in ['OpenAI', 'Claude'])]
    for i, rule in enumerate(ai_rules):
        print(f"AI服务规则 {i+1}: {rule}")
    
    # 测试获取去广告规则
    print("\n测试获取去广告规则...")
    adblock_rules = get_adblock_rules()
    print(f"获取到 {len(adblock_rules)} 条去广告规则")
    for i, rule in enumerate(adblock_rules[:5]):
        print(f"去广告规则 {i+1}: {rule}")
    if len(adblock_rules) > 5:
        print(f"... 还有 {len(adblock_rules) - 5} 条规则")
    
    # 测试获取所有规则集
    print("\n测试获取所有规则集...")
    rulesets = fetch_rulesets(['streaming', 'social', 'ai'])
    adblock_rules = get_adblock_rules()
    all_rules = rulesets + adblock_rules
    print(f"获取到 {len(all_rules)} 条规则")
    
    # 将所有规则保存到文件
    with open('rules.json', 'w', encoding='utf-8') as f:
        json.dump(all_rules, f, ensure_ascii=False, indent=2)
    print("\n所有规则已保存到 rules.json 文件")

if __name__ == "__main__":
    test_rulesets()

