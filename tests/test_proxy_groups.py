#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
策略组生成功能测试脚本
"""

import sys
import os
import json
import yaml

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.proxy_groups import generate_proxy_groups, create_group_by_type
from tests.mock_server import MOCK_CLASH_CONFIG

def test_proxy_groups():
    """测试策略组生成功能"""
    print("测试策略组生成功能...")
    
    # 从模拟的Clash配置中获取节点
    config_dict = yaml.safe_load(MOCK_CLASH_CONFIG)
    nodes = config_dict.get('proxies', [])
    print(f"获取到 {len(nodes)} 个节点")
    
    # 测试生成基础策略组
    print("\n测试生成基础策略组...")
    proxy_groups = generate_proxy_groups(nodes, [])
    print(f"生成了 {len(proxy_groups)} 个策略组")
    for i, group in enumerate(proxy_groups):
        print(f"策略组 {i+1}: {group['name']} ({group['type']})")
        print(f"  代理数量: {len(group['proxies'])}")
    
    # 测试生成流媒体策略组
    print("\n测试生成流媒体策略组...")
    proxy_groups = generate_proxy_groups(nodes, ['streaming'])
    print(f"生成了 {len(proxy_groups)} 个策略组")
    for i, group in enumerate(proxy_groups):
        print(f"策略组 {i+1}: {group['name']} ({group['type']})")
        print(f"  代理数量: {len(group['proxies'])}")
    
    # 测试生成社交媒体策略组
    print("\n测试生成社交媒体策略组...")
    proxy_groups = generate_proxy_groups(nodes, ['social'])
    print(f"生成了 {len(proxy_groups)} 个策略组")
    for i, group in enumerate(proxy_groups):
        print(f"策略组 {i+1}: {group['name']} ({group['type']})")
        print(f"  代理数量: {len(group['proxies'])}")
    
    # 测试生成AI服务策略组
    print("\n测试生成AI服务策略组...")
    proxy_groups = generate_proxy_groups(nodes, ['ai'])
    print(f"生成了 {len(proxy_groups)} 个策略组")
    for i, group in enumerate(proxy_groups):
        print(f"策略组 {i+1}: {group['name']} ({group['type']})")
        print(f"  代理数量: {len(group['proxies'])}")
    
    # 测试生成所有策略组
    print("\n测试生成所有策略组...")
    proxy_groups = generate_proxy_groups(nodes, ['streaming', 'social', 'ai'])
    print(f"生成了 {len(proxy_groups)} 个策略组")
    for i, group in enumerate(proxy_groups):
        print(f"策略组 {i+1}: {group['name']} ({group['type']})")
        print(f"  代理数量: {len(group['proxies'])}")
    
    # 将所有策略组保存到文件
    with open('proxy_groups.json', 'w', encoding='utf-8') as f:
        json.dump(proxy_groups, f, ensure_ascii=False, indent=2)
    print("\n所有策略组已保存到 proxy_groups.json 文件")

if __name__ == "__main__":
    test_proxy_groups()

