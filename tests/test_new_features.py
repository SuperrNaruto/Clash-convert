#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试新的策略组和规则集功能
"""

import os
import sys
import subprocess
import time
import threading
import http.server
import socketserver
import base64

def create_mock_subscription():
    """创建模拟订阅内容"""
    # 创建一些测试节点
    clash_config = {
        'proxies': [
            {
                'name': '测试节点1',
                'type': 'ss',
                'server': '1.2.3.4',
                'port': 8388,
                'cipher': 'aes-256-gcm',
                'password': 'test123'
            },
            {
                'name': '测试节点2',
                'type': 'vmess',
                'server': '5.6.7.8',
                'port': 443,
                'uuid': '12345678-1234-1234-1234-123456789abc',
                'alterId': 0,
                'cipher': 'auto'
            }
        ]
    }
    
    import yaml
    return yaml.dump(clash_config, default_flow_style=False, allow_unicode=True)

class MockHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/subscription':
            # 返回Clash配置
            content = create_mock_subscription()
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(content.encode('utf-8'))))
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        elif self.path == '/subscription_base64':
            # 返回Base64编码的订阅
            v2ray_links = [
                'vmess://eyJ2IjoiMiIsInBzIjoi5rWL6K+V6IqC54K5MSIsImFkZCI6IjEuMi4zLjQiLCJwb3J0IjoiNDQzIiwidHlwZSI6Im5vbmUiLCJpZCI6IjEyMzQ1Njc4LTEyMzQtMTIzNC0xMjM0LTEyMzQ1Njc4OWFiYyIsImFpZCI6IjAiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwiaG9zdCI6IiIsInRscyI6InRscyJ9',
                'ss://YWVzLTI1Ni1nY206dGVzdDEyM0A1LjYuNy44Ojg4ODg=#测试节点2'
            ]
            content = '\n'.join(v2ray_links)
            encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(encoded_content)))
            self.end_headers()
            self.wfile.write(encoded_content.encode('utf-8'))
        else:
            self.send_error(404)

def start_mock_server(port):
    """启动模拟HTTP服务器"""
    handler = MockHTTPHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"模拟HTTP服务器启动在端口 {port}")
        httpd.serve_forever()

def test_conversion(test_name, url, args, project_dir):
    """测试订阅转换功能"""
    print(f"\n=== 测试: {test_name} ===")
    
    output_file = f"test_{test_name.lower().replace(' ', '_').replace('+', '_')}.yaml"
    main_py_path = os.path.join(project_dir, 'main.py')
    cmd = [sys.executable, main_py_path, url, '-o', output_file] + args
    
    print(f"执行命令: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, cwd=project_dir)
        
        if result.returncode == 0:
            print("✅ 转换成功")
            print("输出:")
            print(result.stdout)
            
            # 检查输出文件
            output_path = os.path.join(project_dir, output_file)
            if os.path.exists(output_path):
                file_size = os.path.getsize(output_path)
                print(f"输出文件大小: {file_size} 字节")
                
                # 读取并验证配置文件
                with open(output_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"配置文件行数: {len(content.splitlines())}")
                
                return True
            else:
                print("❌ 输出文件不存在")
                return False
        else:
            print("❌ 转换失败")
            print("错误输出:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ 转换超时")
        return False
    except Exception as e:
        print(f"❌ 测试异常: {str(e)}")
        return False

def main():
    """主测试函数"""
    print("=== 新策略组和规则集功能测试 ===")
    
    # 获取项目根目录
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"项目目录: {project_dir}")
    
    # 查找可用端口
    import socket
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()
    
    # 启动模拟服务器
    server_thread = threading.Thread(target=start_mock_server, args=(port,), daemon=True)
    server_thread.start()
    time.sleep(2)  # 等待服务器启动
    
    base_url = f"http://localhost:{port}"
    
    # 测试用例
    test_cases = [
        ("基础功能", f"{base_url}/subscription", []),
        ("所有策略组", f"{base_url}/subscription", ["--all"]),
        ("流媒体+AI", f"{base_url}/subscription", ["--include-streaming", "--include-ai"]),
        ("社交媒体+广告拦截", f"{base_url}/subscription", ["--include-social", "--include-adblock"]),
        ("科技巨头+游戏", f"{base_url}/subscription", ["--include-techgiants", "--include-gaming"]),
        ("金融+购物", f"{base_url}/subscription", ["--include-finance", "--include-shopping"]),
        ("新闻+开发工具", f"{base_url}/subscription", ["--include-news", "--include-developer"]),
        ("Base64订阅", f"{base_url}/subscription_base64", ["--include-streaming", "--include-social"]),
    ]
    
    # 执行测试
    success_count = 0
    total_count = len(test_cases)
    
    for test_name, url, args in test_cases:
        if test_conversion(test_name, url, args, project_dir):
            success_count += 1
        time.sleep(1)  # 避免请求过快
    
    # 测试结果
    print(f"\n=== 测试结果 ===")
    print(f"总测试数: {total_count}")
    print(f"成功数: {success_count}")
    print(f"失败数: {total_count - success_count}")
    print(f"成功率: {success_count/total_count*100:.1f}%")
    
    if success_count == total_count:
        print("🎉 所有测试通过!")
    else:
        print("⚠️ 部分测试失败")
    
    # 清理测试文件
    print("\n清理测试文件...")
    for test_name, _, _ in test_cases:
        output_file = f"test_{test_name.lower().replace(' ', '_').replace('+', '_')}.yaml"
        output_path = os.path.join(project_dir, output_file)
        if os.path.exists(output_path):
            os.remove(output_path)
            print(f"删除: {output_file}")

if __name__ == "__main__":
    main()

