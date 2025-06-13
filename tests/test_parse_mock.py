#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
订阅解析功能测试脚本（使用模拟数据）
"""

import sys
import os
import json
import base64

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.subscription import parse_subscription, is_base64, is_clash_config

# 模拟的Clash配置数据
MOCK_CLASH_CONFIG = """
port: 7890
socks-port: 7891
allow-lan: true
mode: Rule
log-level: info
external-controller: 127.0.0.1:9090

proxies:
  - name: "节点1"
    type: ss
    server: server1.example.com
    port: 443
    cipher: chacha20-ietf-poly1305
    password: password1
  
  - name: "节点2"
    type: vmess
    server: server2.example.com
    port: 443
    uuid: a3482e88-686a-4a58-8126-99c9df64b7bf
    alterId: 0
    cipher: auto
    tls: true
    network: ws
    ws-path: /path
    ws-headers:
      Host: example.com
  
  - name: "节点3"
    type: trojan
    server: server3.example.com
    port: 443
    password: password3
    sni: example.com
"""

# 模拟的Base64编码订阅数据（包含VMess节点）
MOCK_VMESS_NODE = {
    "v": "2",
    "ps": "测试节点",
    "add": "example.com",
    "port": "443",
    "id": "a3482e88-686a-4a58-8126-99c9df64b7bf",
    "aid": "0",
    "net": "ws",
    "type": "none",
    "host": "example.com",
    "path": "/path",
    "tls": "tls"
}

def create_mock_base64_subscription():
    """创建模拟的Base64编码订阅内容"""
    vmess_url = "vmess://" + base64.b64encode(json.dumps(MOCK_VMESS_NODE).encode()).decode()
    return base64.b64encode(vmess_url.encode()).decode()

def test_parse_clash_config():
    """测试解析Clash配置"""
    print("测试解析Clash配置...")
    try:
        nodes = parse_subscription(MOCK_CLASH_CONFIG)
        print(f"解析到 {len(nodes)} 个节点")
        
        # 打印节点信息
        for i, node in enumerate(nodes):
            print(f"\n节点 {i+1}:")
            print(f"  名称: {node.get('name', 'Unknown')}")
            print(f"  类型: {node.get('type', 'Unknown')}")
            print(f"  服务器: {node.get('server', 'Unknown')}")
            print(f"  端口: {node.get('port', 'Unknown')}")
        
        return True
    except Exception as e:
        print(f"错误: {str(e)}")
        return False

def test_parse_base64_subscription():
    """测试解析Base64编码的订阅"""
    print("\n测试解析Base64编码的订阅...")
    try:
        # 创建模拟的Base64编码订阅内容
        content = create_mock_base64_subscription()
        print(f"Base64编码订阅内容: {content[:30]}...")
        
        # 验证是否为Base64编码
        if is_base64(content):
            print("订阅类型: Base64编码")
        else:
            print("订阅类型: 不是Base64编码")
            return False
        
        # 解析订阅内容
        nodes = parse_subscription(content)
        print(f"解析到 {len(nodes)} 个节点")
        
        # 打印节点信息
        for i, node in enumerate(nodes):
            print(f"\n节点 {i+1}:")
            print(f"  名称: {node.get('name', 'Unknown')}")
            print(f"  类型: {node.get('type', 'Unknown')}")
            print(f"  服务器: {node.get('server', 'Unknown')}")
            print(f"  端口: {node.get('port', 'Unknown')}")
        
        return True
    except Exception as e:
        print(f"错误: {str(e)}")
        return False

if __name__ == "__main__":
    # 测试解析Clash配置
    test_parse_clash_config()
    
    # 测试解析Base64编码的订阅
    test_parse_base64_subscription()

