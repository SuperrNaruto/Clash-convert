# 新的策略组分类和规则映射设计

## 策略组分类设计

基于blackmatrix7/ios_rule_script仓库的丰富规则集，我们将设计以下策略组分类：

### 1. 流媒体服务组 (Streaming)
#### 国际流媒体
- 🎬 Netflix: Netflix流媒体服务
- 🎵 Spotify: Spotify音乐流媒体
- 📺 YouTube: YouTube视频服务
- 🎭 Disney+: Disney Plus流媒体
- 🎪 HBO: HBO流媒体服务
- 📽️ Amazon Prime Video: 亚马逊Prime视频
- 🎨 Hulu: Hulu流媒体服务
- 🎪 Paramount+: Paramount Plus流媒体

#### 亚洲流媒体
- 📺 哔哩哔哩: B站视频服务
- 🎭 AcFun: A站视频服务
- 📱 AbemaTV: 日本流媒体服务
- 🎬 iQIYI: 爱奇艺视频
- 📺 Youku: 优酷视频
- 🎵 NetEaseMusic: 网易云音乐
- 🎶 QQMusic: QQ音乐

### 2. 社交媒体组 (Social)
#### 即时通讯
- 💬 Telegram: 电报
- 💬 WhatsApp: WhatsApp
- 💬 Line: Line通讯
- 💬 WeChat: 微信
- 💬 Discord: Discord

#### 社交平台
- 📘 Facebook: Facebook社交平台
- 📷 Instagram: Instagram图片社交
- 🐦 Twitter: Twitter微博
- 💼 LinkedIn: LinkedIn职业社交
- 📌 Pinterest: Pinterest图片分享
- 🎵 TikTok: TikTok短视频
- 📱 Snapchat: Snapchat

### 3. AI服务组 (AI)
- 🤖 OpenAI: OpenAI/ChatGPT服务
- 🧠 Claude: Anthropic Claude AI
- 🔍 Bing AI: 微软Bing AI
- 🎨 Midjourney: Midjourney AI绘画
- 📝 Notion AI: Notion AI服务

### 4. 科技巨头组 (TechGiants)
#### 苹果服务
- 🍎 Apple: 苹果公司服务
- 📱 App Store: 苹果应用商店
- ☁️ iCloud: 苹果云服务
- 🎵 Apple Music: 苹果音乐
- 📺 Apple TV: 苹果电视服务

#### 谷歌服务
- 🔍 Google: 谷歌搜索和服务
- 📧 Gmail: 谷歌邮箱
- 📱 Google Play: 谷歌应用商店
- ☁️ Google Drive: 谷歌云盘
- 📺 YouTube: YouTube视频

#### 微软服务
- 🪟 Microsoft: 微软服务
- 📧 Outlook: 微软邮箱
- ☁️ OneDrive: 微软云盘
- 💼 Office365: 微软办公套件
- 🎮 Xbox: Xbox游戏服务

#### 亚马逊服务
- 📦 Amazon: 亚马逊购物
- ☁️ AWS: 亚马逊云服务
- 📺 Prime Video: 亚马逊视频
- 🎵 Amazon Music: 亚马逊音乐

### 5. 游戏服务组 (Gaming)
- 🎮 Steam: Steam游戏平台
- 🎮 Epic Games: Epic游戏商店
- 🎮 PlayStation: 索尼PlayStation
- 🎮 Xbox: 微软Xbox
- 🎮 Nintendo: 任天堂服务
- 🎮 Blizzard: 暴雪游戏
- 🎮 EA: EA游戏
- 🎮 Ubisoft: 育碧游戏

### 6. 金融服务组 (Finance)
- 💳 PayPal: PayPal支付
- 💰 支付宝: 阿里支付宝
- 💳 微信支付: 腾讯微信支付
- 🏦 银行服务: 各大银行应用
- 📈 股票交易: 股票交易平台

### 7. 购物电商组 (Shopping)
- 🛒 Amazon: 亚马逊购物
- 🛍️ 淘宝: 阿里淘宝
- 🛒 京东: 京东购物
- 🛍️ eBay: eBay购物
- 🛒 拼多多: 拼多多购物

### 8. 新闻媒体组 (News)
- 📰 BBC: 英国广播公司
- 📺 CNN: 美国有线电视新闻网
- 📰 Reuters: 路透社
- 📺 Fox News: 福克斯新闻
- 📰 新浪: 新浪新闻
- 📺 央视: 中央电视台

### 9. 开发工具组 (Developer)
- 💻 GitHub: GitHub代码托管
- 💻 GitLab: GitLab代码托管
- 💻 Stack Overflow: 程序员问答
- 💻 Docker: Docker容器
- 💻 npm: Node.js包管理

### 10. 广告拦截组 (AdBlock)
- 🛡️ 广告拦截: 通用广告拦截规则
- 🛡️ 隐私保护: 隐私追踪拦截
- 🛡️ 恶意软件: 恶意软件拦截

## 规则集映射

### blackmatrix7仓库规则集映射表

| 策略组 | 规则集名称 | 描述 |
|--------|------------|------|
| Netflix | Netflix | Netflix流媒体服务 |
| Spotify | Spotify | Spotify音乐服务 |
| YouTube | YouTube | YouTube视频服务 |
| Disney+ | Disney | Disney Plus流媒体 |
| 哔哩哔哩 | BiliBili | B站视频服务 |
| Telegram | Telegram | 电报通讯 |
| Facebook | Facebook | Facebook社交 |
| Instagram | Instagram | Instagram图片社交 |
| Twitter | Twitter | Twitter微博 |
| OpenAI | OpenAI | OpenAI/ChatGPT |
| Claude | Anthropic | Anthropic Claude |
| Apple | Apple | 苹果服务 |
| Google | Google | 谷歌服务 |
| Microsoft | Microsoft | 微软服务 |
| Amazon | Amazon | 亚马逊服务 |
| Steam | Steam | Steam游戏平台 |
| PayPal | PayPal | PayPal支付 |
| 支付宝 | AliPay | 支付宝 |
| GitHub | GitHub | GitHub代码托管 |
| 广告拦截 | Advertising | 广告拦截规则 |

## 策略组优先级设计

1. **高优先级**: AI服务、流媒体、社交媒体
2. **中优先级**: 科技巨头、游戏服务、金融服务
3. **低优先级**: 购物电商、新闻媒体、开发工具
4. **系统级**: 广告拦截、隐私保护

## 规则集URL模板

blackmatrix7仓库的规则集URL格式：
```
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/{RuleName}/{RuleName}.yaml
```

例如：
- Netflix: `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Netflix/Netflix.yaml`
- Telegram: `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.yaml`

