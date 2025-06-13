#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clash订阅转换程序使用示例 v2.0

本示例展示了如何使用新版本的Clash订阅转换程序，
包括多种策略组类型和从blackmatrix7仓库获取规则集的功能。
"""

import os
import sys
import subprocess

def run_command(cmd, description):
    """运行命令并显示结果"""
    print(f"\n{'='*60}")
    print(f"示例: {description}")
    print(f"命令: {' '.join(cmd)}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("✅ 执行成功")
            print("\n输出:")
            print(result.stdout)
        else:
            print("❌ 执行失败")
            print("\n错误:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("⏰ 执行超时")
    except Exception as e:
        print(f"❌ 执行异常: {str(e)}")

def main():
    """主函数"""
    print("Clash订阅转换程序使用示例 v2.0")
    print("=" * 60)
    
    # 检查是否在正确的目录
    if not os.path.exists('main.py'):
        print("错误: 请在程序根目录下运行此示例")
        sys.exit(1)
    
    # 示例订阅链接（请替换为您的实际订阅链接）
    subscription_url = "https://your-subscription-url-here"
    
    print(f"注意: 请将示例中的订阅链接替换为您的实际订阅链接")
    print(f"当前使用的示例链接: {subscription_url}")
    
    # 示例1: 查看程序信息
    run_command(
        [sys.executable, 'main.py', '--info'],
        "查看规则集信息"
    )
    
    # 示例2: 列出所有策略组类型
    run_command(
        [sys.executable, 'main.py', '--list-groups'],
        "列出所有可用的策略组类型"
    )
    
    # 示例3: 显示帮助信息
    run_command(
        [sys.executable, 'main.py', '--help'],
        "显示详细帮助信息"
    )
    
    print(f"\n{'='*60}")
    print("以下示例需要有效的订阅链接才能正常运行")
    print("请将 subscription_url 变量替换为您的实际订阅链接")
    print(f"{'='*60}")
    
    # 如果用户提供了订阅链接参数，则运行转换示例
    if len(sys.argv) > 1:
        subscription_url = sys.argv[1]
        print(f"使用提供的订阅链接: {subscription_url}")
        
        # 示例4: 基础转换（使用默认策略组）
        run_command(
            [sys.executable, 'main.py', subscription_url, '-o', 'example_basic.yaml'],
            "基础转换 - 使用默认策略组（流媒体、社交媒体、AI服务、广告拦截）"
        )
        
        # 示例5: 全功能转换
        run_command(
            [sys.executable, 'main.py', subscription_url, '--all', '-o', 'example_full.yaml', '--verbose'],
            "全功能转换 - 包含所有策略组类型"
        )
        
        # 示例6: 流媒体爱好者配置
        run_command(
            [sys.executable, 'main.py', subscription_url, 
             '--include-streaming', '--include-social', '--include-adblock',
             '-o', 'example_streaming.yaml'],
            "流媒体爱好者配置"
        )
        
        # 示例7: 开发者配置
        run_command(
            [sys.executable, 'main.py', subscription_url,
             '--include-developer', '--include-techgiants', '--include-ai', '--include-adblock',
             '-o', 'example_developer.yaml'],
            "开发者配置"
        )
        
        # 示例8: 游戏玩家配置
        run_command(
            [sys.executable, 'main.py', subscription_url,
             '--include-gaming', '--include-social', '--include-streaming', '--include-adblock',
             '-o', 'example_gaming.yaml'],
            "游戏玩家配置"
        )
        
        # 示例9: 商务办公配置
        run_command(
            [sys.executable, 'main.py', subscription_url,
             '--include-techgiants', '--include-finance', '--include-shopping', '--include-news', '--include-adblock',
             '-o', 'example_business.yaml'],
            "商务办公配置"
        )
        
        # 示例10: 强制更新（不使用缓存）
        run_command(
            [sys.executable, 'main.py', subscription_url,
             '--include-streaming', '--include-ai', '--no-cache',
             '-o', 'example_no_cache.yaml'],
            "强制更新 - 不使用缓存重新获取规则集"
        )
        
        # 清理生成的示例文件
        print(f"\n{'='*60}")
        print("清理生成的示例文件")
        print(f"{'='*60}")
        
        example_files = [
            'example_basic.yaml',
            'example_full.yaml', 
            'example_streaming.yaml',
            'example_developer.yaml',
            'example_gaming.yaml',
            'example_business.yaml',
            'example_no_cache.yaml'
        ]
        
        for file in example_files:
            if os.path.exists(file):
                os.remove(file)
                print(f"删除: {file}")
        
        print("\n✅ 所有示例执行完成!")
        
    else:
        print("\n💡 提示:")
        print("要运行转换示例，请提供订阅链接作为参数:")
        print(f"python {sys.argv[0]} https://your-subscription-url")
        
        print("\n📋 可用的命令行选项:")
        print("--all                    包含所有策略组")
        print("--include-streaming      包含流媒体策略组")
        print("--include-social         包含社交媒体策略组")
        print("--include-ai             包含AI服务策略组")
        print("--include-techgiants     包含科技巨头策略组")
        print("--include-gaming         包含游戏服务策略组")
        print("--include-finance        包含金融服务策略组")
        print("--include-shopping       包含购物电商策略组")
        print("--include-news           包含新闻媒体策略组")
        print("--include-developer      包含开发工具策略组")
        print("--include-adblock        包含广告拦截策略组")
        print("--no-cache               不使用缓存")
        print("--verbose                显示详细输出")
        print("-o FILE                  指定输出文件")
        
        print("\n🎯 推荐配置组合:")
        print("影音娱乐: --include-streaming --include-social --include-adblock")
        print("程序开发: --include-developer --include-techgiants --include-ai --include-adblock")
        print("游戏玩家: --include-gaming --include-social --include-streaming --include-adblock")
        print("商务办公: --include-techgiants --include-finance --include-news --include-adblock")
        print("学生用户: --include-streaming --include-social --include-adblock")

if __name__ == "__main__":
    main()

