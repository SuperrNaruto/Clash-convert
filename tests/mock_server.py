#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模拟HTTP服务器，用于提供订阅内容
"""

import http.server
import socketserver
import json
import base64
import yaml
import threading
import time
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 模拟的Clash配置数据
MOCK_CLASH_CONFIG = """
port: 7890
socks-port: 7891
allow-lan: true
mode: Rule
log-level: info
external-controller: 127.0.0.1:9090

proxies:
  - name: "Node1"
    type: ss
    server: server1.example.com
    port: 443
    cipher: chacha20-ietf-poly1305
    password: password1
  
  - name: "Node2"
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
  
  - name: "Node3"
    type: trojan
    server: server3.example.com
    port: 443
    password: password3
    sni: example.com
"""

# 模拟的VMess节点
MOCK_VMESS_NODE = {
    "v": "2",
    "ps": "TestNode",
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

class MockHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """模拟HTTP请求处理器"""
    
    def do_GET(self):
        """处理GET请求"""
        if self.path == '/clash':
            # 返回Clash配置
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(MOCK_CLASH_CONFIG.encode('utf-8'))
        elif self.path == '/base64':
            # 返回Base64编码的订阅内容
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(create_mock_base64_subscription().encode('utf-8'))
        else:
            # 返回404
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        """禁止输出日志"""
        return

def start_mock_server(port=8000):
    """启动模拟HTTP服务器"""
    handler = MockHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    print(f"启动模拟HTTP服务器在端口 {port}")
    print(f"Clash配置: http://localhost:{port}/clash")
    print(f"Base64编码订阅: http://localhost:{port}/base64")
    
    # 在新线程中启动服务器
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    return httpd

if __name__ == "__main__":
    # 启动模拟HTTP服务器
    httpd = start_mock_server()
    
    try:
        # 保持程序运行
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 关闭服务器
        httpd.shutdown()
        print("服务器已关闭")

