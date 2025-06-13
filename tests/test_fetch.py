#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试从模拟HTTP服务器获取订阅内容
"""

import sys
import os
import json
import time
import threading

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.subscription import fetch_subscription, parse_subscription
from tests.mock_server import start_mock_server

def test_fetch_subscription():
    """测试从模拟HTTP服务器获取订阅内容"""
    # 启动模拟HTTP服务器
    port = 8000
    httpd = start_mock_server(port)
    
    try:
        # 等待服务器启动
        time.sleep(1)
        
        # 测试获取Clash配置
        print("\n测试获取Clash配置...")
        clash_url = f"http://localhost:{port}/clash"
        try:
            content = fetch_subscription(clash_url)
            print(f"获取到内容长度: {len(content)} 字节")
            print("内容预览:")
            print(content[:200] + "...")
            
            # 解析内容
            nodes = parse_subscription(content)
            print(f"解析到 {len(nodes)} 个节点")
        except Exception as e:
            print(f"错误: {str(e)}")
        
        # 测试获取Base64编码的订阅内容
        print("\n测试获取Base64编码的订阅内容...")
        base64_url = f"http://localhost:{port}/base64"
        try:
            content = fetch_subscription(base64_url)
            print(f"获取到内容长度: {len(content)} 字节")
            print("内容预览:")
            print(content[:50] + "...")
            
            # 解析内容
            nodes = parse_subscription(content)
            print(f"解析到 {len(nodes)} 个节点")
        except Exception as e:
            print(f"错误: {str(e)}")
        
    finally:
        # 关闭服务器
        httpd.shutdown()
        print("\n服务器已关闭")

if __name__ == "__main__":
    test_fetch_subscription()

