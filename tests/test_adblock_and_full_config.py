#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
去广告规则获取和配置文件生成测试脚本
"""

import sys
import os
import yaml
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.subscription import fetch_subscription, parse_subscription
from modules.proxy_groups import generate_proxy_groups
from modules.rulesets import fetch_rulesets, get_adblock_rules, fetch_ruleset_files
from modules.generator import generate_config, save_config
from tests.mock_server import MOCK_CLASH_CONFIG, start_mock_server
import time

def test_adblock_rules():
    """测试去广告规则获取功能"""
    print("测试去广告规则获取功能...")
    
    # 获取去广告规则
    print("\n获取去广告规则...")
    adblock_rules = get_adblock_rules()
    print(f"获取到 {len(adblock_rules)} 条去广告规则")
    
    # 查看本地去广告规则文件
    adblock_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'rules', 'adblock.list')
    if os.path.exists(adblock_file):
        with open(adblock_file, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"\n本地去广告规则文件内容预览 ({adblock_file}):")
        lines = content.strip().split('\n')
        for i, line in enumerate(lines[:10]):
            print(f"{i+1}: {line}")
        if len(lines) > 10:
            print(f"... 还有 {len(lines) - 10} 条规则")
    
    return adblock_rules

def test_full_config_generation():
    """测试完整配置文件生成功能"""
    print("\n测试完整配置文件生成功能...")
    
    # 启动模拟HTTP服务器
    port = 8000
    httpd = start_mock_server(port)
    
    try:
        # 等待服务器启动
        time.sleep(1)
        
        # 获取订阅内容
        print("\n获取订阅内容...")
        url = f"http://localhost:{port}/clash"
        content = fetch_subscription(url)
        print(f"获取到内容长度: {len(content)} 字节")
        
        # 解析订阅内容
        print("\n解析订阅内容...")
        nodes = parse_subscription(content)
        print(f"解析到 {len(nodes)} 个节点")
        
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
        print("\n生成完整配置文件...")
        config_content = generate_config(nodes, proxy_groups, all_rules)
        print(f"生成的配置文件大小: {len(config_content)} 字节")
        
        # 保存配置文件
        output_path = 'full_config.yaml'
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
            
            # 检查是否包含去广告规则
            adblock_rule_count = 0
            for rule in config.get('rules', []):
                if '广告拦截' in rule:
                    adblock_rule_count += 1
            
            if adblock_rule_count >= len(adblock_rules):
                print(f"✓ 包含去广告规则: {adblock_rule_count} 条")
            else:
                print(f"✗ 去广告规则数量不正确: 期望 {len(adblock_rules)}, 实际 {adblock_rule_count}")
            
            print("\n完整配置文件生成成功!")
            print(f"配置文件已保存到: {os.path.abspath(output_path)}")
            
        except Exception as e:
            print(f"验证配置文件失败: {str(e)}")
    
    finally:
        # 关闭服务器
        httpd.shutdown()
        print("\n服务器已关闭")

if __name__ == "__main__":
    # 测试去广告规则获取功能
    adblock_rules = test_adblock_rules()
    
    # 测试完整配置文件生成功能
    test_full_config_generation()

