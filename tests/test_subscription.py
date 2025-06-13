#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
订阅获取和解析功能测试脚本
"""

import sys
import os
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.subscription import fetch_subscription, parse_subscription, is_base64, is_clash_config

def test_subscription(url):
    """测试订阅获取和解析功能"""
    print(f"正在获取订阅: {url}")
    try:
        # 获取订阅内容
        content = fetch_subscription(url)
        print(f"订阅内容长度: {len(content)} 字节")
        
        # 判断订阅类型
        if is_base64(content):
            print("订阅类型: Base64编码")
        elif is_clash_config(content):
            print("订阅类型: Clash配置")
        else:
            print("订阅类型: 未知")
        
        # 解析订阅内容
        nodes = parse_subscription(content)
        print(f"解析到 {len(nodes)} 个节点")
        
        # 打印前5个节点的信息
        for i, node in enumerate(nodes[:5]):
            print(f"\n节点 {i+1}:")
            print(f"  名称: {node.get('name', 'Unknown')}")
            print(f"  类型: {node.get('type', 'Unknown')}")
            print(f"  服务器: {node.get('server', 'Unknown')}")
            print(f"  端口: {node.get('port', 'Unknown')}")
        
        # 将所有节点保存到文件
        with open('nodes.json', 'w', encoding='utf-8') as f:
            json.dump(nodes, f, ensure_ascii=False, indent=2)
        print("\n所有节点已保存到 nodes.json 文件")
        
        return True
    except Exception as e:
        print(f"错误: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python test_subscription.py <订阅链接>")
        sys.exit(1)
    
    url = sys.argv[1]
    test_subscription(url)

