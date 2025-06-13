#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试主程序功能
"""

import sys
import os
import subprocess
import time
import threading

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.mock_server import start_mock_server

def run_main_program(url, output_path, include_all=False):
    """运行主程序"""
    cmd = [
        'python3',
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'main.py'),
        url,
        '-o', output_path
    ]
    
    if include_all:
        cmd.append('--all')
    
    print(f"运行命令: {' '.join(cmd)}")
    
    # 运行主程序
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    
    # 打印输出
    print("\n标准输出:")
    print(stdout)
    
    if stderr:
        print("\n标准错误:")
        print(stderr)
    
    return process.returncode

def test_main_program():
    """测试主程序功能"""
    print("测试主程序功能...")
    
    # 启动模拟HTTP服务器
    port = 8888  # 使用不同的端口
    httpd = start_mock_server(port)
    
    try:
        # 等待服务器启动
        time.sleep(1)
        
        # 测试Clash配置订阅
        print("\n测试Clash配置订阅...")
        url = f"http://localhost:{port}/clash"
        output_path = 'main_test_clash.yaml'
        returncode = run_main_program(url, output_path, include_all=True)
        
        if returncode == 0:
            print(f"\n✓ 主程序成功处理Clash配置订阅")
            print(f"配置文件已保存到: {os.path.abspath(output_path)}")
        else:
            print(f"\n✗ 主程序处理Clash配置订阅失败，返回码: {returncode}")
        
        # 测试Base64编码订阅
        print("\n测试Base64编码订阅...")
        url = f"http://localhost:{port}/base64"
        output_path = 'main_test_base64.yaml'
        returncode = run_main_program(url, output_path, include_all=True)
        
        if returncode == 0:
            print(f"\n✓ 主程序成功处理Base64编码订阅")
            print(f"配置文件已保存到: {os.path.abspath(output_path)}")
        else:
            print(f"\n✗ 主程序处理Base64编码订阅失败，返回码: {returncode}")
        
    finally:
        # 关闭服务器
        httpd.shutdown()
        print("\n服务器已关闭")

if __name__ == "__main__":
    test_main_program()

