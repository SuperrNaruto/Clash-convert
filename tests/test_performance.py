#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
程序性能测试和优化脚本
"""

import sys
import os
import time
import cProfile
import pstats
import io
import threading
import random

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.subscription import fetch_subscription, parse_subscription
from modules.proxy_groups import generate_proxy_groups
from modules.rulesets import fetch_rulesets, get_adblock_rules, load_cache, save_cache
from modules.generator import generate_config, save_config
from tests.mock_server import start_mock_server

def profile_function(func, *args, **kwargs):
    """使用cProfile分析函数性能"""
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()
    
    # 获取性能统计信息
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(20)  # 打印前20个耗时最长的函数
    
    return result, s.getvalue()

def test_performance():
    """测试程序性能"""
    print("测试程序性能...")
    
    # 加载缓存
    load_cache()
    
    # 启动模拟HTTP服务器
    port = random.randint(10000, 20000)  # 使用随机端口
    print(f"使用端口: {port}")
    httpd = start_mock_server(port)
    
    try:
        # 等待服务器启动
        time.sleep(1)
        
        # 测试订阅获取性能
        print("\n测试订阅获取性能...")
        url = f"http://localhost:{port}/clash"
        start_time = time.time()
        _, profile_result = profile_function(fetch_subscription, url)
        end_time = time.time()
        print(f"订阅获取耗时: {end_time - start_time:.4f} 秒")
        print("\n性能分析结果:")
        print(profile_result)
        
        # 获取订阅内容
        subscription_content = fetch_subscription(url)
        
        # 测试订阅解析性能
        print("\n测试订阅解析性能...")
        start_time = time.time()
        _, profile_result = profile_function(parse_subscription, subscription_content)
        end_time = time.time()
        print(f"订阅解析耗时: {end_time - start_time:.4f} 秒")
        print("\n性能分析结果:")
        print(profile_result)
        
        # 获取节点
        nodes = parse_subscription(subscription_content)
        
        # 测试策略组生成性能
        print("\n测试策略组生成性能...")
        start_time = time.time()
        _, profile_result = profile_function(generate_proxy_groups, nodes, ['streaming', 'social', 'ai'])
        end_time = time.time()
        print(f"策略组生成耗时: {end_time - start_time:.4f} 秒")
        print("\n性能分析结果:")
        print(profile_result)
        
        # 获取策略组
        proxy_groups = generate_proxy_groups(nodes, ['streaming', 'social', 'ai'])
        
        # 测试规则集获取性能
        print("\n测试规则集获取性能...")
        start_time = time.time()
        _, profile_result = profile_function(fetch_rulesets, ['streaming', 'social', 'ai'])
        end_time = time.time()
        print(f"规则集获取耗时: {end_time - start_time:.4f} 秒")
        print("\n性能分析结果:")
        print(profile_result)
        
        # 获取规则集
        rulesets = fetch_rulesets(['streaming', 'social', 'ai'])
        
        # 测试去广告规则获取性能
        print("\n测试去广告规则获取性能...")
        start_time = time.time()
        _, profile_result = profile_function(get_adblock_rules)
        end_time = time.time()
        print(f"去广告规则获取耗时: {end_time - start_time:.4f} 秒")
        print("\n性能分析结果:")
        print(profile_result)
        
        # 获取去广告规则
        adblock_rules = get_adblock_rules()
        
        # 合并规则
        all_rules = rulesets + adblock_rules
        
        # 测试配置文件生成性能
        print("\n测试配置文件生成性能...")
        start_time = time.time()
        _, profile_result = profile_function(generate_config, nodes, proxy_groups, all_rules)
        end_time = time.time()
        print(f"配置文件生成耗时: {end_time - start_time:.4f} 秒")
        print("\n性能分析结果:")
        print(profile_result)
        
        # 测试整体性能
        print("\n测试整体性能...")
        start_time = time.time()
        
        # 获取订阅内容
        subscription_content = fetch_subscription(url)
        
        # 解析订阅内容
        nodes = parse_subscription(subscription_content)
        
        # 生成策略组
        proxy_groups = generate_proxy_groups(nodes, ['streaming', 'social', 'ai'])
        
        # 获取规则集
        rulesets = fetch_rulesets(['streaming', 'social', 'ai'])
        
        # 获取去广告规则
        adblock_rules = get_adblock_rules()
        
        # 合并规则
        all_rules = rulesets + adblock_rules
        
        # 生成配置文件
        config_content = generate_config(nodes, proxy_groups, all_rules)
        
        # 保存配置文件
        save_config(config_content, 'performance_test.yaml')
        
        end_time = time.time()
        print(f"整体处理耗时: {end_time - start_time:.4f} 秒")
        
        # 保存缓存
        save_cache()
        
    finally:
        # 关闭服务器
        httpd.shutdown()
        print("\n服务器已关闭")

def test_error_handling():
    """测试错误处理"""
    print("\n测试错误处理...")
    
    # 测试无效URL
    print("\n测试无效URL...")
    try:
        fetch_subscription("http://invalid.url")
        print("✗ 未能正确处理无效URL")
    except Exception as e:
        print(f"✓ 正确处理无效URL: {str(e)}")
    
    # 测试无效订阅内容
    print("\n测试无效订阅内容...")
    try:
        parse_subscription("invalid content")
        print("✗ 未能正确处理无效订阅内容")
    except Exception as e:
        print(f"✓ 正确处理无效订阅内容: {str(e)}")
    
    # 测试空节点列表
    print("\n测试空节点列表...")
    try:
        proxy_groups = generate_proxy_groups([])
        print(f"✓ 正确处理空节点列表，生成了 {len(proxy_groups)} 个策略组")
    except Exception as e:
        print(f"✗ 未能正确处理空节点列表: {str(e)}")

if __name__ == "__main__":
    # 测试程序性能
    test_performance()
    
    # 测试错误处理
    test_error_handling()

