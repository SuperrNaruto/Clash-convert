#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置文件

包含程序运行所需的各种配置信息，包括规则集URL、策略组配置等。
"""

import os

# 基础配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, '..', '..', 'templates')
RULES_DIR = os.path.join(BASE_DIR, '..', '..', 'rules')

# 网络请求配置
REQUEST_TIMEOUT = 30
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# blackmatrix7 规则集URL配置
BLACKMATRIX7_BASE_URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash"

# 规则集URL映射 (使用blackmatrix7仓库)
RULESET_URLS = {
    # 流媒体服务
    'streaming': {
        'netflix': f"{BLACKMATRIX7_BASE_URL}/Netflix/Netflix.yaml",
        'spotify': f"{BLACKMATRIX7_BASE_URL}/Spotify/Spotify.yaml",
        'youtube': f"{BLACKMATRIX7_BASE_URL}/YouTube/YouTube.yaml",
        'disney': f"{BLACKMATRIX7_BASE_URL}/Disney/Disney.yaml",
        'hbo': f"{BLACKMATRIX7_BASE_URL}/HBO/HBO.yaml",
        'amazonprimevideo': f"{BLACKMATRIX7_BASE_URL}/AmazonPrimeVideo/AmazonPrimeVideo.yaml",
        'hulu': f"{BLACKMATRIX7_BASE_URL}/Hulu/Hulu.yaml",
        'paramount': f"{BLACKMATRIX7_BASE_URL}/ParamountPlus/ParamountPlus.yaml",
        'bilibili': f"{BLACKMATRIX7_BASE_URL}/BiliBili/BiliBili.yaml",
        'acfun': f"{BLACKMATRIX7_BASE_URL}/AcFun/AcFun.yaml",
        'abematv': f"{BLACKMATRIX7_BASE_URL}/AbemaTV/AbemaTV.yaml",
        'iqiyi': f"{BLACKMATRIX7_BASE_URL}/iQIYI/iQIYI.yaml",
        'youku': f"{BLACKMATRIX7_BASE_URL}/Youku/Youku.yaml",
        'neteasemusic': f"{BLACKMATRIX7_BASE_URL}/NetEaseMusic/NetEaseMusic.yaml",
        'qqmusic': f"{BLACKMATRIX7_BASE_URL}/QQMusic/QQMusic.yaml",
    },
    
    # 社交媒体
    'social': {
        'telegram': f"{BLACKMATRIX7_BASE_URL}/Telegram/Telegram.yaml",
        'whatsapp': f"{BLACKMATRIX7_BASE_URL}/WhatsApp/WhatsApp.yaml",
        'line': f"{BLACKMATRIX7_BASE_URL}/Line/Line.yaml",
        'wechat': f"{BLACKMATRIX7_BASE_URL}/WeChat/WeChat.yaml",
        'discord': f"{BLACKMATRIX7_BASE_URL}/Discord/Discord.yaml",
        'facebook': f"{BLACKMATRIX7_BASE_URL}/Facebook/Facebook.yaml",
        'instagram': f"{BLACKMATRIX7_BASE_URL}/Instagram/Instagram.yaml",
        'twitter': f"{BLACKMATRIX7_BASE_URL}/Twitter/Twitter.yaml",
        'linkedin': f"{BLACKMATRIX7_BASE_URL}/LinkedIn/LinkedIn.yaml",
        'pinterest': f"{BLACKMATRIX7_BASE_URL}/Pinterest/Pinterest.yaml",
        'tiktok': f"{BLACKMATRIX7_BASE_URL}/TikTok/TikTok.yaml",
        'snapchat': f"{BLACKMATRIX7_BASE_URL}/Snapchat/Snapchat.yaml",
    },
    
    # AI服务
    'ai': {
        'openai': f"{BLACKMATRIX7_BASE_URL}/OpenAI/OpenAI.yaml",
        'anthropic': f"{BLACKMATRIX7_BASE_URL}/Anthropic/Anthropic.yaml",
        'bing': f"{BLACKMATRIX7_BASE_URL}/Bing/Bing.yaml",
        'midjourney': f"{BLACKMATRIX7_BASE_URL}/Midjourney/Midjourney.yaml",
        'notion': f"{BLACKMATRIX7_BASE_URL}/Notion/Notion.yaml",
    },
    
    # 科技巨头
    'techgiants': {
        'apple': f"{BLACKMATRIX7_BASE_URL}/Apple/Apple.yaml",
        'appstore': f"{BLACKMATRIX7_BASE_URL}/AppStore/AppStore.yaml",
        'icloud': f"{BLACKMATRIX7_BASE_URL}/iCloud/iCloud.yaml",
        'applemusic': f"{BLACKMATRIX7_BASE_URL}/AppleMusic/AppleMusic.yaml",
        'appletv': f"{BLACKMATRIX7_BASE_URL}/AppleTV/AppleTV.yaml",
        'google': f"{BLACKMATRIX7_BASE_URL}/Google/Google.yaml",
        'gmail': f"{BLACKMATRIX7_BASE_URL}/Gmail/Gmail.yaml",
        'googleplay': f"{BLACKMATRIX7_BASE_URL}/GooglePlay/GooglePlay.yaml",
        'googledrive': f"{BLACKMATRIX7_BASE_URL}/GoogleDrive/GoogleDrive.yaml",
        'microsoft': f"{BLACKMATRIX7_BASE_URL}/Microsoft/Microsoft.yaml",
        'outlook': f"{BLACKMATRIX7_BASE_URL}/Outlook/Outlook.yaml",
        'onedrive': f"{BLACKMATRIX7_BASE_URL}/OneDrive/OneDrive.yaml",
        'office365': f"{BLACKMATRIX7_BASE_URL}/Office365/Office365.yaml",
        'xbox': f"{BLACKMATRIX7_BASE_URL}/Xbox/Xbox.yaml",
        'amazon': f"{BLACKMATRIX7_BASE_URL}/Amazon/Amazon.yaml",
        'aws': f"{BLACKMATRIX7_BASE_URL}/AWS/AWS.yaml",
    },
    
    # 游戏服务
    'gaming': {
        'steam': f"{BLACKMATRIX7_BASE_URL}/Steam/Steam.yaml",
        'epicgames': f"{BLACKMATRIX7_BASE_URL}/Epic/Epic.yaml",
        'playstation': f"{BLACKMATRIX7_BASE_URL}/PlayStation/PlayStation.yaml",
        'nintendo': f"{BLACKMATRIX7_BASE_URL}/Nintendo/Nintendo.yaml",
        'blizzard': f"{BLACKMATRIX7_BASE_URL}/Blizzard/Blizzard.yaml",
        'ea': f"{BLACKMATRIX7_BASE_URL}/EA/EA.yaml",
        'ubisoft': f"{BLACKMATRIX7_BASE_URL}/Ubisoft/Ubisoft.yaml",
    },
    
    # 金融服务
    'finance': {
        'paypal': f"{BLACKMATRIX7_BASE_URL}/PayPal/PayPal.yaml",
        'alipay': f"{BLACKMATRIX7_BASE_URL}/AliPay/AliPay.yaml",
    },
    
    # 购物电商
    'shopping': {
        'taobao': f"{BLACKMATRIX7_BASE_URL}/Taobao/Taobao.yaml",
        'jd': f"{BLACKMATRIX7_BASE_URL}/JD/JD.yaml",
        'ebay': f"{BLACKMATRIX7_BASE_URL}/eBay/eBay.yaml",
        'pdd': f"{BLACKMATRIX7_BASE_URL}/PDD/PDD.yaml",
    },
    
    # 新闻媒体
    'news': {
        'bbc': f"{BLACKMATRIX7_BASE_URL}/BBC/BBC.yaml",
        'cnn': f"{BLACKMATRIX7_BASE_URL}/CNN/CNN.yaml",
        'reuters': f"{BLACKMATRIX7_BASE_URL}/Reuters/Reuters.yaml",
        'foxnews': f"{BLACKMATRIX7_BASE_URL}/FoxNews/FoxNews.yaml",
        'sina': f"{BLACKMATRIX7_BASE_URL}/Sina/Sina.yaml",
    },
    
    # 开发工具
    'developer': {
        'github': f"{BLACKMATRIX7_BASE_URL}/GitHub/GitHub.yaml",
        'gitlab': f"{BLACKMATRIX7_BASE_URL}/GitLab/GitLab.yaml",
        'stackoverflow': f"{BLACKMATRIX7_BASE_URL}/StackOverflow/StackOverflow.yaml",
        'docker': f"{BLACKMATRIX7_BASE_URL}/Docker/Docker.yaml",
        'npm': f"{BLACKMATRIX7_BASE_URL}/npm/npm.yaml",
    },
    
    # 广告拦截
    'adblock': {
        'advertising': f"{BLACKMATRIX7_BASE_URL}/Advertising/Advertising.yaml",
        'advertisinglite': f"{BLACKMATRIX7_BASE_URL}/AdvertisingLite/AdvertisingLite.yaml",
        'advertisingmitv': f"{BLACKMATRIX7_BASE_URL}/AdvertisingMiTV/AdvertisingMiTV.yaml",
        'privacy': f"{BLACKMATRIX7_BASE_URL}/Privacy/Privacy.yaml",
        'hijacking': f"{BLACKMATRIX7_BASE_URL}/Hijacking/Hijacking.yaml",
    }
}

# 模板文件路径
TEMPLATE_CONFIG = os.path.join(TEMPLATES_DIR, 'config.yaml')
TEMPLATE_GROUPS = {
    'streaming': os.path.join(TEMPLATES_DIR, 'groups', 'streaming.yaml'),
    'social': os.path.join(TEMPLATES_DIR, 'groups', 'social.yaml'),
    'ai': os.path.join(TEMPLATES_DIR, 'groups', 'ai.yaml'),
    'techgiants': os.path.join(TEMPLATES_DIR, 'groups', 'techgiants.yaml'),
    'gaming': os.path.join(TEMPLATES_DIR, 'groups', 'gaming.yaml'),
    'finance': os.path.join(TEMPLATES_DIR, 'groups', 'finance.yaml'),
    'shopping': os.path.join(TEMPLATES_DIR, 'groups', 'shopping.yaml'),
    'news': os.path.join(TEMPLATES_DIR, 'groups', 'news.yaml'),
    'developer': os.path.join(TEMPLATES_DIR, 'groups', 'developer.yaml'),
    'adblock': os.path.join(TEMPLATES_DIR, 'groups', 'adblock.yaml'),
}

# 策略组类型配置
GROUP_TYPES = {
    'streaming': {
        'name': '流媒体服务',
        'description': 'Netflix, YouTube, Spotify等流媒体服务',
        'icon': '🎬',
        'color': 'red'
    },
    'social': {
        'name': '社交媒体',
        'description': 'Telegram, Twitter, Facebook, Instagram等',
        'icon': '💬',
        'color': 'blue'
    },
    'ai': {
        'name': 'AI服务',
        'description': 'OpenAI, Claude, Bing AI等',
        'icon': '🤖',
        'color': 'purple'
    },
    'techgiants': {
        'name': '科技巨头',
        'description': 'Apple, Google, Microsoft, Amazon服务',
        'icon': '🏢',
        'color': 'green'
    },
    'gaming': {
        'name': '游戏服务',
        'description': 'Steam, Epic Games, PlayStation等',
        'icon': '🎮',
        'color': 'orange'
    },
    'finance': {
        'name': '金融服务',
        'description': 'PayPal, 支付宝等支付平台',
        'icon': '💰',
        'color': 'yellow'
    },
    'shopping': {
        'name': '购物电商',
        'description': 'Amazon, 淘宝, 京东, eBay等',
        'icon': '🛒',
        'color': 'pink'
    },
    'news': {
        'name': '新闻媒体',
        'description': 'BBC, CNN, Reuters等新闻网站',
        'icon': '📰',
        'color': 'indigo'
    },
    'developer': {
        'name': '开发工具',
        'description': 'GitHub, GitLab, Docker等',
        'icon': '💻',
        'color': 'gray'
    },
    'adblock': {
        'name': '广告拦截',
        'description': '广告和追踪器拦截规则',
        'icon': '🛡️',
        'color': 'emerald'
    }
}

# 预设配置
PRESET_CONFIGS = {
    'default': {
        'name': '默认配置',
        'description': '流媒体、社交媒体、AI服务、广告拦截',
        'groups': ['streaming', 'social', 'ai', 'adblock']
    },
    'entertainment': {
        'name': '影音娱乐',
        'description': '适合观看视频、听音乐的用户',
        'groups': ['streaming', 'social', 'adblock']
    },
    'developer': {
        'name': '程序开发',
        'description': '适合软件开发人员',
        'groups': ['techgiants', 'developer', 'ai', 'adblock']
    },
    'gaming': {
        'name': '游戏玩家',
        'description': '适合游戏爱好者',
        'groups': ['gaming', 'social', 'streaming', 'adblock']
    },
    'business': {
        'name': '商务办公',
        'description': '适合商务和办公场景',
        'groups': ['techgiants', 'finance', 'shopping', 'news', 'adblock']
    }
}


