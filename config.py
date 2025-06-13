#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
配置文件

包含程序运行所需的各种配置信息，包括规则集URL、策略组配置等。
"""

import os

# 基础配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
RULES_DIR = os.path.join(BASE_DIR, 'rules')

# 网络请求配置
REQUEST_TIMEOUT = 30
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# blackmatrix7 规则集URL配置
BLACKMATRIX7_BASE_URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash"

# 规则集URL映射 (使用blackmatrix7仓库)
RULESET_URLS = {
    # 流媒体服务
    'netflix': f"{BLACKMATRIX7_BASE_URL}/Netflix/Netflix.yaml",
    'spotify': f"{BLACKMATRIX7_BASE_URL}/Spotify/Spotify.yaml",
    'youtube': f"{BLACKMATRIX7_BASE_URL}/YouTube/YouTube.yaml",
    'disney': f"{BLACKMATRIX7_BASE_URL}/Disney/Disney.yaml",
    'hbo': f"{BLACKMATRIX7_BASE_URL}/HBO/HBO.yaml",
    'amazonprimevideo': f"{BLACKMATRIX7_BASE_URL}/AmazonPrimeVideo/AmazonPrimeVideo.yaml",
    'hulu': f"{BLACKMATRIX7_BASE_URL}/Hulu/Hulu.yaml",
    'paramount': f"{BLACKMATRIX7_BASE_URL}/ParamountPlus/ParamountPlus.yaml",
    
    # 亚洲流媒体
    'bilibili': f"{BLACKMATRIX7_BASE_URL}/BiliBili/BiliBili.yaml",
    'acfun': f"{BLACKMATRIX7_BASE_URL}/AcFun/AcFun.yaml",
    'abematv': f"{BLACKMATRIX7_BASE_URL}/AbemaTV/AbemaTV.yaml",
    'iqiyi': f"{BLACKMATRIX7_BASE_URL}/iQIYI/iQIYI.yaml",
    'youku': f"{BLACKMATRIX7_BASE_URL}/Youku/Youku.yaml",
    'neteasemusic': f"{BLACKMATRIX7_BASE_URL}/NetEaseMusic/NetEaseMusic.yaml",
    'qqmusic': f"{BLACKMATRIX7_BASE_URL}/QQMusic/QQMusic.yaml",
    
    # 社交媒体
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
    
    # AI服务
    'openai': f"{BLACKMATRIX7_BASE_URL}/OpenAI/OpenAI.yaml",
    'anthropic': f"{BLACKMATRIX7_BASE_URL}/Anthropic/Anthropic.yaml",
    'bing': f"{BLACKMATRIX7_BASE_URL}/Bing/Bing.yaml",
    'midjourney': f"{BLACKMATRIX7_BASE_URL}/Midjourney/Midjourney.yaml",
    'notion': f"{BLACKMATRIX7_BASE_URL}/Notion/Notion.yaml",
    
    # 科技巨头
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
    
    # 游戏服务
    'steam': f"{BLACKMATRIX7_BASE_URL}/Steam/Steam.yaml",
    'epicgames': f"{BLACKMATRIX7_BASE_URL}/Epic/Epic.yaml",
    'playstation': f"{BLACKMATRIX7_BASE_URL}/PlayStation/PlayStation.yaml",
    'nintendo': f"{BLACKMATRIX7_BASE_URL}/Nintendo/Nintendo.yaml",
    'blizzard': f"{BLACKMATRIX7_BASE_URL}/Blizzard/Blizzard.yaml",
    'ea': f"{BLACKMATRIX7_BASE_URL}/EA/EA.yaml",
    'ubisoft': f"{BLACKMATRIX7_BASE_URL}/Ubisoft/Ubisoft.yaml",
    
    # 金融服务
    'paypal': f"{BLACKMATRIX7_BASE_URL}/PayPal/PayPal.yaml",
    'alipay': f"{BLACKMATRIX7_BASE_URL}/AliPay/AliPay.yaml",
    
    # 购物电商
    'taobao': f"{BLACKMATRIX7_BASE_URL}/Taobao/Taobao.yaml",
    'jd': f"{BLACKMATRIX7_BASE_URL}/JD/JD.yaml",
    'ebay': f"{BLACKMATRIX7_BASE_URL}/eBay/eBay.yaml",
    'pdd': f"{BLACKMATRIX7_BASE_URL}/PDD/PDD.yaml",
    
    # 新闻媒体
    'bbc': f"{BLACKMATRIX7_BASE_URL}/BBC/BBC.yaml",
    'cnn': f"{BLACKMATRIX7_BASE_URL}/CNN/CNN.yaml",
    'reuters': f"{BLACKMATRIX7_BASE_URL}/Reuters/Reuters.yaml",
    'foxnews': f"{BLACKMATRIX7_BASE_URL}/FoxNews/FoxNews.yaml",
    'sina': f"{BLACKMATRIX7_BASE_URL}/Sina/Sina.yaml",
    
    # 开发工具
    'github': f"{BLACKMATRIX7_BASE_URL}/GitHub/GitHub.yaml",
    'gitlab': f"{BLACKMATRIX7_BASE_URL}/GitLab/GitLab.yaml",
    'stackoverflow': f"{BLACKMATRIX7_BASE_URL}/StackOverflow/StackOverflow.yaml",
    'docker': f"{BLACKMATRIX7_BASE_URL}/Docker/Docker.yaml",
    'npm': f"{BLACKMATRIX7_BASE_URL}/npm/npm.yaml",
    
    # 广告拦截
    'advertising': f"{BLACKMATRIX7_BASE_URL}/Advertising/Advertising.yaml",
    'advertisinglite': f"{BLACKMATRIX7_BASE_URL}/AdvertisingLite/AdvertisingLite.yaml",
    'advertisingmitv': f"{BLACKMATRIX7_BASE_URL}/AdvertisingMiTV/AdvertisingMiTV.yaml",
    'privacy': f"{BLACKMATRIX7_BASE_URL}/Privacy/Privacy.yaml",
    'hijacking': f"{BLACKMATRIX7_BASE_URL}/Hijacking/Hijacking.yaml",
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

# 基础规则集
BASE_RULES = [
    'RULE-SET,applications,DIRECT',
    'DOMAIN,clash.razord.top,DIRECT',
    'DOMAIN,yacd.haishan.me,DIRECT',
    'RULE-SET,private,DIRECT',
    'RULE-SET,reject,🛑 广告拦截',
    'RULE-SET,icloud,DIRECT',
    'RULE-SET,apple,DIRECT',
    'RULE-SET,google,🚀 节点选择',
    'RULE-SET,tld-not-cn,🚀 节点选择',
    'RULE-SET,gfw,🚀 节点选择',
    'RULE-SET,telegramcidr,🚀 节点选择,no-resolve',
    'GEOIP,LAN,DIRECT',
    'GEOIP,CN,DIRECT',
    'MATCH,🐟 漏网之鱼'
]

# 流媒体规则集
STREAMING_RULES = [
    'RULE-SET,netflix,🎬 Netflix',
    'RULE-SET,spotify,🎵 Spotify', 
    'RULE-SET,youtube,📺 YouTube',
    'RULE-SET,disney,🎭 Disney+',
    'RULE-SET,hbo,🎪 HBO',
    'RULE-SET,amazonprimevideo,📽️ Amazon Prime Video',
    'RULE-SET,hulu,🎨 Hulu',
    'RULE-SET,paramount,🎪 Paramount+',
    'RULE-SET,bilibili,📺 哔哩哔哩',
    'RULE-SET,acfun,🎭 AcFun',
    'RULE-SET,abematv,📱 AbemaTV',
    'RULE-SET,iqiyi,🎬 爱奇艺',
    'RULE-SET,youku,📺 优酷',
    'RULE-SET,neteasemusic,🎵 网易云音乐',
    'RULE-SET,qqmusic,🎶 QQ音乐',
]

# 社交媒体规则集
SOCIAL_RULES = [
    'RULE-SET,telegram,💬 Telegram',
    'RULE-SET,whatsapp,💬 WhatsApp',
    'RULE-SET,line,💬 Line',
    'RULE-SET,wechat,💬 微信',
    'RULE-SET,discord,💬 Discord',
    'RULE-SET,facebook,📘 Facebook',
    'RULE-SET,instagram,📷 Instagram',
    'RULE-SET,twitter,🐦 Twitter',
    'RULE-SET,linkedin,💼 LinkedIn',
    'RULE-SET,pinterest,📌 Pinterest',
    'RULE-SET,tiktok,🎵 TikTok',
    'RULE-SET,snapchat,📱 Snapchat',
]

# AI服务规则集
AI_RULES = [
    'RULE-SET,openai,🤖 OpenAI',
    'RULE-SET,anthropic,🧠 Claude',
    'RULE-SET,bing,🔍 Bing AI',
    'RULE-SET,midjourney,🎨 Midjourney',
    'RULE-SET,notion,📝 Notion AI',
]

# 科技巨头规则集
TECHGIANTS_RULES = [
    'RULE-SET,apple,🍎 Apple',
    'RULE-SET,appstore,📱 App Store',
    'RULE-SET,icloud,☁️ iCloud',
    'RULE-SET,applemusic,🎵 Apple Music',
    'RULE-SET,appletv,📺 Apple TV',
    'RULE-SET,google,🔍 Google',
    'RULE-SET,gmail,📧 Gmail',
    'RULE-SET,googleplay,📱 Google Play',
    'RULE-SET,googledrive,☁️ Google Drive',
    'RULE-SET,microsoft,🪟 Microsoft',
    'RULE-SET,outlook,📧 Outlook',
    'RULE-SET,onedrive,☁️ OneDrive',
    'RULE-SET,office365,💼 Office365',
    'RULE-SET,xbox,🎮 Xbox',
    'RULE-SET,amazon,📦 Amazon',
    'RULE-SET,aws,☁️ AWS',
]

# 游戏服务规则集
GAMING_RULES = [
    'RULE-SET,steam,🎮 Steam',
    'RULE-SET,epicgames,🎮 Epic Games',
    'RULE-SET,playstation,🎮 PlayStation',
    'RULE-SET,nintendo,🎮 Nintendo',
    'RULE-SET,blizzard,🎮 Blizzard',
    'RULE-SET,ea,🎮 EA',
    'RULE-SET,ubisoft,🎮 Ubisoft',
]

# 金融服务规则集
FINANCE_RULES = [
    'RULE-SET,paypal,💳 PayPal',
    'RULE-SET,alipay,💰 支付宝',
]

# 购物电商规则集
SHOPPING_RULES = [
    'RULE-SET,amazon,🛒 Amazon',
    'RULE-SET,taobao,🛍️ 淘宝',
    'RULE-SET,jd,🛒 京东',
    'RULE-SET,ebay,🛍️ eBay',
    'RULE-SET,pdd,🛒 拼多多',
]

# 新闻媒体规则集
NEWS_RULES = [
    'RULE-SET,bbc,📰 BBC',
    'RULE-SET,cnn,📺 CNN',
    'RULE-SET,reuters,📰 Reuters',
    'RULE-SET,foxnews,📺 Fox News',
    'RULE-SET,sina,📰 新浪',
]

# 开发工具规则集
DEVELOPER_RULES = [
    'RULE-SET,github,💻 GitHub',
    'RULE-SET,gitlab,💻 GitLab',
    'RULE-SET,stackoverflow,💻 Stack Overflow',
    'RULE-SET,docker,💻 Docker',
    'RULE-SET,npm,💻 npm',
]

# 广告拦截规则集
ADBLOCK_RULES = [
    'RULE-SET,advertising,🛡️ 广告拦截',
    'RULE-SET,advertisinglite,🛡️ 广告拦截',
    'RULE-SET,advertisingmitv,🛡️ 广告拦截',
    'RULE-SET,privacy,🛡️ 隐私保护',
    'RULE-SET,hijacking,🛡️ 恶意软件',
]

# 策略组类型映射
GROUP_TYPE_MAPPING = {
    'streaming': STREAMING_RULES,
    'social': SOCIAL_RULES,
    'ai': AI_RULES,
    'techgiants': TECHGIANTS_RULES,
    'gaming': GAMING_RULES,
    'finance': FINANCE_RULES,
    'shopping': SHOPPING_RULES,
    'news': NEWS_RULES,
    'developer': DEVELOPER_RULES,
    'adblock': ADBLOCK_RULES,
}

