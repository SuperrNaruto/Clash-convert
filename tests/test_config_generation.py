#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置生成功能测试脚本
"""

import sys
import os
import yaml
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.subscription import parse_subscription
from modules.proxy_groups import generate_proxy_groups
from modules.rulesets import fetch_rulesets, get_adblock_rules
from modules.generator import generate_config, save_config
from tests.mock_server import MOCK_CLASH_CONFIG

def test_config_generation():
    """测试配置生成功能"""
    print("测试配置生成功能...")
    
    # 从模拟的Clash配置中获取节点
    config_dict = yaml.safe_load(MOCK_CLASH_CONFIG)
    nodes = config_dict.get('proxies', [])
    print(f"获取到 {len(nodes)} 个节点")
    
    # 生成策略组
    print("\n生成策略组...")
    proxy_groups = generate_proxy_groups(nodes, ['streaming', 'social', 'ai'])
    print(f"生成了 {len(proxy_groups)} 个策略组")
    
    # 获取规则集
    print("\n获取规则集...")
    rulesets = fetch_rulesets(['streaming', 'social', 'ai'])
    print(f"获取到 {len(rulesets)} 条规则")
    
    # 获取去广告规则
    print("\n获取去广告规则...")
    adblock_rules = get_adblock_rules()
    print(f"获取到 {len(adblock_rules)} 条去广告规则")
    
    # 合并规则
    all_rules = rulesets + adblock_rules
    
    # 生成配置文件
    print("\n生成配置文件...")
    config_content = generate_config(nodes, proxy_groups, all_rules)
    print(f"生成的配置文件大小: {len(config_content)} 字节")
    
    # 保存配置文件
    output_path = 'test_config.yaml'
    print(f"\n保存配置文件到: {output_path}")
    save_config(config_content, output_path)
    
    # 验证生成的配置文件
    print("\n验证生成的配置文件...")
    try:
        with open(output_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # 检查配置文件的关键部分
        if 'proxies' in config and len(config['proxies']) == len(nodes):
            print(f"✓ 代理节点数量正确: {len(config['proxies'])}")
        else:
            print(f"✗ 代理节点数量不正确: 期望 {len(nodes)}, 实际 {len(config.get('proxies', []))}")
        
        if 'proxy-groups' in config and len(config['proxy-groups']) == len(proxy_groups):
            print(f"✓ 策略组数量正确: {len(config['proxy-groups'])}")
        else:
            print(f"✗ 策略组数量不正确: 期望 {len(proxy_groups)}, 实际 {len(config.get('proxy-groups', []))}")
        
        if 'rules' in config and len(config['rules']) == len(all_rules):
            print(f"✓ 规则数量正确: {len(config['rules'])}")
        else:
            print(f"✗ 规则数量不正确: 期望 {len(all_rules)}, 实际 {len(config.get('rules', []))}")
        
        print("\n配置文件生成成功!")
        print(f"配置文件已保存到: {os.path.abspath(output_path)}")
        
    except Exception as e:
        print(f"验证配置文件失败: {str(e)}")

if __name__ == "__main__":
    test_config_generation()

