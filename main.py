#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clash订阅转换程序主入口

支持将各种订阅链接转换为具有完整精细分流规则的Clash配置文件，
包括多个策略组（流媒体、社交媒体、AI服务、科技巨头、游戏服务、
金融服务、购物电商、新闻媒体、开发工具和广告拦截）。

使用blackmatrix7/ios_rule_script仓库的高质量规则集。
"""

import argparse
import sys
import os

# 添加模块路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.subscription import fetch_subscription, parse_subscription
from modules.proxy_groups import generate_all_groups, get_available_group_types
from modules.rulesets import get_rulesets_for_groups, generate_rules_for_groups, load_cache, save_cache, get_ruleset_info
from modules.generator import generate_clash_config

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='Clash订阅转换程序 - 支持多种策略组和精细分流规则',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  %(prog)s https://example.com/subscription -o config.yaml --all
  %(prog)s https://example.com/subscription --include-streaming --include-ai
  %(prog)s https://example.com/subscription --include-social --include-adblock
  
策略组类型:
  streaming   - 流媒体服务 (Netflix, YouTube, Spotify等)
  social      - 社交媒体 (Telegram, Twitter, Facebook等)
  ai          - AI服务 (OpenAI, Claude, Bing AI等)
  techgiants  - 科技巨头 (Apple, Google, Microsoft, Amazon)
  gaming      - 游戏服务 (Steam, Epic Games, PlayStation等)
  finance     - 金融服务 (PayPal, 支付宝等)
  shopping    - 购物电商 (Amazon, 淘宝, 京东等)
  news        - 新闻媒体 (BBC, CNN, Reuters等)
  developer   - 开发工具 (GitHub, GitLab, Docker等)
  adblock     - 广告拦截 (广告、隐私保护、恶意软件拦截)
        """
    )
    
    parser.add_argument('url', nargs='?', help='订阅链接URL')
    parser.add_argument('-o', '--output', default='clash_config.yaml', help='输出文件路径 (默认: clash_config.yaml)')
    
    # 策略组选项
    group_options = parser.add_argument_group('策略组选项')
    group_options.add_argument('--all', action='store_true', help='包含所有策略组和规则')
    group_options.add_argument('--include-streaming', action='store_true', help='包含流媒体策略组')
    group_options.add_argument('--include-social', action='store_true', help='包含社交媒体策略组')
    group_options.add_argument('--include-ai', action='store_true', help='包含AI服务策略组')
    group_options.add_argument('--include-techgiants', action='store_true', help='包含科技巨头策略组')
    group_options.add_argument('--include-gaming', action='store_true', help='包含游戏服务策略组')
    group_options.add_argument('--include-finance', action='store_true', help='包含金融服务策略组')
    group_options.add_argument('--include-shopping', action='store_true', help='包含购物电商策略组')
    group_options.add_argument('--include-news', action='store_true', help='包含新闻媒体策略组')
    group_options.add_argument('--include-developer', action='store_true', help='包含开发工具策略组')
    group_options.add_argument('--include-adblock', action='store_true', help='包含广告拦截策略组')
    
    # 其他选项
    other_options = parser.add_argument_group('其他选项')
    other_options.add_argument('--info', action='store_true', help='显示规则集信息')
    other_options.add_argument('--list-groups', action='store_true', help='列出所有可用的策略组类型')
    other_options.add_argument('--no-cache', action='store_true', help='不使用缓存，强制重新获取规则集')
    other_options.add_argument('--verbose', '-v', action='store_true', help='显示详细输出')
    
    args = parser.parse_args()
    
    # 如果是信息查询选项，不需要url参数
    if args.info or args.list_groups:
        return args
    
    # 其他情况需要url参数
    if not args.url:
        parser.error("订阅链接URL是必需的参数（除非使用 --info 或 --list-groups 选项）")
    
    return args

def determine_group_types(args):
    """根据命令行参数确定要包含的策略组类型"""
    if args.all:
        return get_available_group_types()
    
    group_types = []
    
    if args.include_streaming:
        group_types.append('streaming')
    if args.include_social:
        group_types.append('social')
    if args.include_ai:
        group_types.append('ai')
    if args.include_techgiants:
        group_types.append('techgiants')
    if args.include_gaming:
        group_types.append('gaming')
    if args.include_finance:
        group_types.append('finance')
    if args.include_shopping:
        group_types.append('shopping')
    if args.include_news:
        group_types.append('news')
    if args.include_developer:
        group_types.append('developer')
    if args.include_adblock:
        group_types.append('adblock')
    
    # 如果没有指定任何策略组，默认包含基础组合
    if not group_types:
        group_types = ['streaming', 'social', 'ai', 'adblock']
        print("未指定策略组类型，使用默认组合: 流媒体、社交媒体、AI服务、广告拦截")
    
    return group_types

def show_ruleset_info():
    """显示规则集信息"""
    info = get_ruleset_info()
    
    print("=== Clash订阅转换程序 - 规则集信息 ===")
    print(f"规则集来源: {info['source']}")
    print(f"总规则集数量: {info['total_rulesets']}")
    print(f"缓存有效期: {info['cache_expiry_hours']} 小时")
    print("\n各类别规则集数量:")
    
    category_names = {
        'streaming': '流媒体服务',
        'social': '社交媒体',
        'ai': 'AI服务',
        'techgiants': '科技巨头',
        'gaming': '游戏服务',
        'finance': '金融服务',
        'shopping': '购物电商',
        'news': '新闻媒体',
        'developer': '开发工具',
        'adblock': '广告拦截',
    }
    
    for category, count in info['categories'].items():
        name = category_names.get(category, category)
        print(f"  {name}: {count} 个规则集")

def show_available_groups():
    """显示所有可用的策略组类型"""
    print("=== 可用的策略组类型 ===")
    
    group_descriptions = {
        'streaming': '流媒体服务 - Netflix, YouTube, Spotify, Disney+, 哔哩哔哩等',
        'social': '社交媒体 - Telegram, Twitter, Facebook, Instagram, Discord等',
        'ai': 'AI服务 - OpenAI/ChatGPT, Claude, Bing AI, Midjourney等',
        'techgiants': '科技巨头 - Apple, Google, Microsoft, Amazon服务',
        'gaming': '游戏服务 - Steam, Epic Games, PlayStation, Xbox等',
        'finance': '金融服务 - PayPal, 支付宝等',
        'shopping': '购物电商 - Amazon, 淘宝, 京东, eBay等',
        'news': '新闻媒体 - BBC, CNN, Reuters, Fox News等',
        'developer': '开发工具 - GitHub, GitLab, Docker, npm等',
        'adblock': '广告拦截 - 广告、隐私保护、恶意软件拦截',
    }
    
    for group_type in get_available_group_types():
        description = group_descriptions.get(group_type, '未知类型')
        print(f"  {group_type:12} - {description}")

def main():
    """主函数"""
    args = parse_arguments()
    
    # 显示信息选项
    if args.info:
        show_ruleset_info()
        return
    
    if args.list_groups:
        show_available_groups()
        return
    
    # 加载缓存
    if not args.no_cache:
        load_cache()
    
    try:
        print("=== Clash订阅转换程序 ===")
        print(f"订阅链接: {args.url}")
        print(f"输出文件: {args.output}")
        
        # 获取订阅内容
        print("\n1. 正在获取订阅内容...")
        subscription_content = fetch_subscription(args.url)
        if not subscription_content:
            print("错误: 无法获取订阅内容")
            sys.exit(1)
        
        # 解析订阅内容
        print("2. 正在解析订阅内容...")
        proxies = parse_subscription(subscription_content)
        if not proxies:
            print("错误: 无法解析订阅内容或订阅中没有有效节点")
            sys.exit(1)
        
        print(f"成功解析 {len(proxies)} 个代理节点")
        
        # 确定策略组类型
        group_types = determine_group_types(args)
        print(f"\n3. 生成策略组类型: {', '.join(group_types)}")
        
        # 生成策略组
        print("4. 正在生成策略组...")
        proxy_names = [proxy['name'] for proxy in proxies]
        proxy_groups = generate_all_groups(proxy_names, group_types)
        print(f"成功生成 {len(proxy_groups)} 个策略组")
        
        # 获取规则集
        print("5. 正在获取分流规则集...")
        rulesets = get_rulesets_for_groups(group_types)
        print(f"成功获取 {len(rulesets)} 个规则集")
        
        # 生成规则列表
        print("6. 正在生成分流规则...")
        rules = generate_rules_for_groups(group_types)
        print(f"成功生成 {len(rules)} 条分流规则")
        
        # 生成配置文件
        print("7. 正在生成Clash配置文件...")
        config = generate_clash_config(proxies, proxy_groups, rules, rulesets)
        
        # 保存配置文件
        print("8. 正在保存配置文件...")
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(config)
        
        print(f"\n✅ 转换完成! 配置文件已保存到: {os.path.abspath(args.output)}")
        
        # 显示统计信息
        print(f"\n📊 统计信息:")
        print(f"  代理节点: {len(proxies)} 个")
        print(f"  策略组: {len(proxy_groups)} 个")
        print(f"  规则集: {len(rulesets)} 个")
        print(f"  分流规则: {len(rules)} 条")
        
        if args.verbose:
            print(f"\n📋 包含的策略组类型:")
            for group_type in group_types:
                print(f"  - {group_type}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断操作")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 转换失败: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)
    finally:
        # 保存缓存
        if not args.no_cache:
            save_cache()

if __name__ == "__main__":
    main()

