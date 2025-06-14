# Clash订阅转换程序 v2.0

一个功能强大的Clash订阅转换程序，支持将各种订阅链接转换为具有完整精细分流规则的Clash配置文件。程序包含多达10种策略组分类，涵盖流媒体、社交媒体、AI服务、科技巨头、游戏服务、金融服务、购物电商、新闻媒体、开发工具和广告拦截等领域。

## ✨ 主要特性

### 🎯 丰富的策略组分类
- **流媒体服务**: Netflix, YouTube, Spotify, Disney+, HBO, Amazon Prime Video, Hulu, Paramount+, 哔哩哔哩, 爱奇艺, 优酷, 网易云音乐等
- **社交媒体**: Telegram, WhatsApp, Line, 微信, Discord, Facebook, Instagram, Twitter, LinkedIn, Pinterest, TikTok, Snapchat等
- **AI服务**: OpenAI/ChatGPT, Claude, Bing AI, Midjourney, Notion AI等
- **科技巨头**: Apple (App Store, iCloud, Apple Music, Apple TV), Google (Gmail, Google Play, Google Drive), Microsoft (Outlook, OneDrive, Office365, Xbox), Amazon (AWS)等
- **游戏服务**: Steam, Epic Games, PlayStation, Nintendo, Blizzard, EA, Ubisoft等
- **金融服务**: PayPal, 支付宝等
- **购物电商**: Amazon, 淘宝, 京东, eBay, 拼多多等
- **新闻媒体**: BBC, CNN, Reuters, Fox News, 新浪等
- **开发工具**: GitHub, GitLab, Stack Overflow, Docker, npm等
- **广告拦截**: 广告、隐私保护、恶意软件拦截等

### 🔧 高质量规则集
- 使用 [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) 仓库的高质量规则集
- 总计76个规则集，覆盖主流应用和服务
- 自动缓存机制，提升转换速度
- 智能错误处理，跳过不可用的规则集

### 📱 多种订阅格式支持
- Clash YAML格式配置文件
- Base64编码的V2Ray/SS/SSR/Trojan订阅
- 自动识别订阅格式并进行相应处理

### ⚡ 性能优化
- 智能缓存系统，规则集缓存24小时
- 并发处理，提升转换速度
- 内存优化，支持大型订阅文件

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 基本使用

```bash
# 使用所有策略组和规则
python main.py https://your-subscription-url -o config.yaml --all

# 使用默认策略组（流媒体、社交媒体、AI服务、广告拦截）
python main.py https://your-subscription-url -o config.yaml

# 自定义策略组组合
python main.py https://your-subscription-url --include-streaming --include-ai --include-adblock
```

### 查看可用选项

```bash
# 显示规则集信息
python main.py --info

# 列出所有策略组类型
python main.py --list-groups

# 显示帮助信息
python main.py --help
```

## 📋 命令行选项

### 基本选项
- `url`: 订阅链接URL（必需，除非使用信息查询选项）
- `-o, --output`: 输出文件路径（默认: clash_config.yaml）

### 策略组选项
- `--all`: 包含所有策略组和规则
- `--include-streaming`: 包含流媒体策略组
- `--include-social`: 包含社交媒体策略组
- `--include-ai`: 包含AI服务策略组
- `--include-techgiants`: 包含科技巨头策略组
- `--include-gaming`: 包含游戏服务策略组
- `--include-finance`: 包含金融服务策略组
- `--include-shopping`: 包含购物电商策略组
- `--include-news`: 包含新闻媒体策略组
- `--include-developer`: 包含开发工具策略组
- `--include-adblock`: 包含广告拦截策略组

### 其他选项
- `--info`: 显示规则集信息
- `--list-groups`: 列出所有可用的策略组类型
- `--no-cache`: 不使用缓存，强制重新获取规则集
- `--verbose, -v`: 显示详细输出

## 📊 规则集统计

| 策略组类型 | 规则集数量 | 主要服务 |
|-----------|-----------|----------|
| 流媒体服务 | 15 | Netflix, YouTube, Spotify, Disney+, 哔哩哔哩等 |
| 社交媒体 | 12 | Telegram, Twitter, Facebook, Instagram, Discord等 |
| AI服务 | 5 | OpenAI, Claude, Bing AI, Midjourney等 |
| 科技巨头 | 16 | Apple, Google, Microsoft, Amazon服务 |
| 游戏服务 | 7 | Steam, Epic Games, PlayStation, Xbox等 |
| 金融服务 | 2 | PayPal, 支付宝 |
| 购物电商 | 5 | Amazon, 淘宝, 京东, eBay等 |
| 新闻媒体 | 5 | BBC, CNN, Reuters等 |
| 开发工具 | 5 | GitHub, GitLab, Docker等 |
| 广告拦截 | 5 | 广告、隐私保护、恶意软件拦截 |

## 🎯 使用示例

### 示例1: 流媒体爱好者配置
```bash
python main.py https://your-subscription-url \
  --include-streaming \
  --include-adblock \
  -o streaming_config.yaml
```

### 示例2: 开发者配置
```bash
python main.py https://your-subscription-url \
  --include-developer \
  --include-techgiants \
  --include-ai \
  --include-adblock \
  -o developer_config.yaml
```

### 示例3: 全功能配置
```bash
python main.py https://your-subscription-url \
  --all \
  -o full_config.yaml \
  --verbose
```

### 示例4: 社交媒体配置
```bash
python main.py https://your-subscription-url \
  --include-social \
  --include-gaming \
  --include-adblock \
  -o social_config.yaml
```

## 🏗️ 项目结构

```
clash_sub_converter/
├── main.py                 # 主程序入口
├── config.py              # 配置文件
├── requirements.txt       # 依赖包列表
├── README.md             # 英文说明文档
├── 使用说明.md           # 中文使用指南
├── LICENSE               # 开源许可证
├── modules/              # 核心模块
│   ├── __init__.py
│   ├── subscription.py   # 订阅获取和解析
│   ├── proxy_groups.py   # 策略组生成
│   ├── rulesets.py      # 规则集获取
│   └── generator.py     # 配置文件生成
├── templates/           # 策略组模板
│   ├── config.yaml     # 基础配置模板
│   └── groups/         # 策略组模板目录
│       ├── streaming.yaml    # 流媒体策略组
│       ├── social.yaml      # 社交媒体策略组
│       ├── ai.yaml          # AI服务策略组
│       ├── techgiants.yaml  # 科技巨头策略组
│       ├── gaming.yaml      # 游戏服务策略组
│       ├── finance.yaml     # 金融服务策略组
│       ├── shopping.yaml    # 购物电商策略组
│       ├── news.yaml        # 新闻媒体策略组
│       ├── developer.yaml   # 开发工具策略组
│       └── adblock.yaml     # 广告拦截策略组
├── cache/              # 缓存目录
├── tests/              # 测试脚本
└── dist/               # 打包输出目录
```

## 🔧 技术特性

### 智能缓存系统
程序采用智能缓存机制，将获取的规则集缓存24小时，大幅提升转换速度：
- 首次获取规则集：约60-120秒
- 使用缓存转换：约1-3秒

### 错误处理机制
- 自动跳过不可用的规则集
- 网络超时重试机制
- 详细的错误日志输出
- 优雅的降级处理

### 配置文件验证
- YAML格式验证
- 必要字段检查
- 代理节点格式验证
- 策略组配置验证

## 🌟 新版本特性 (v2.0)

### 新增策略组类型
- **科技巨头**: 新增Apple、Google、Microsoft、Amazon等大厂服务的精细分流
- **游戏服务**: 支持Steam、Epic Games、PlayStation等游戏平台
- **金融服务**: 支持PayPal、支付宝等支付平台
- **购物电商**: 支持Amazon、淘宝、京东等电商平台
- **新闻媒体**: 支持BBC、CNN、Reuters等新闻网站
- **开发工具**: 支持GitHub、GitLab、Docker等开发工具

### 规则集升级
- 从blackmatrix7/ios_rule_script仓库获取高质量规则集
- 规则集数量从5个增加到76个
- 支持更精细的分流控制
- 定期更新规则集内容

### 性能优化
- 新增智能缓存系统，转换速度提升10倍以上
- 优化内存使用，支持更大的订阅文件
- 改进错误处理，提高程序稳定性

## 📝 配置文件说明

生成的Clash配置文件包含以下主要部分：

### 基础配置
- 端口设置（HTTP: 7890, SOCKS: 7891）
- DNS配置（支持DoH和防污染）
- 日志级别和外部控制器设置

### 代理节点
- 保留原订阅中的所有有效节点
- 支持SS、SSR、V2Ray、Trojan等协议

### 策略组
- **基础策略组**: 节点选择、自动选择、故障转移、负载均衡
- **功能策略组**: 根据选择的类型生成对应的策略组
- **兜底策略组**: 漏网之鱼，处理未匹配的流量

### 分流规则
- 按优先级排列的分流规则
- 支持域名、IP、进程等多种匹配方式
- 自动添加基础规则（局域网、中国大陆等）

## 🛠️ 开发说明

### 添加新的策略组类型

1. 在 `config.py` 中添加规则集URL和映射关系
2. 在 `templates/groups/` 目录下创建对应的YAML模板文件
3. 在 `modules/proxy_groups.py` 中添加生成函数
4. 在 `modules/rulesets.py` 中添加获取函数
5. 更新 `main.py` 中的命令行选项

### 自定义规则集

可以通过修改 `config.py` 文件中的 `RULESET_URLS` 字典来添加自定义规则集：

```python
RULESET_URLS = {
    'custom_service': 'https://example.com/custom_rules.yaml',
    # ... 其他规则集
}
```

### 测试

运行测试脚本验证功能：

```bash
python tests/test_new_features.py
```

## 🐳 Docker部署

使用Docker可以快速运行后端API服务（已包含构建好的前端静态文件）。

### 构建镜像

```bash
docker build -t clash-converter .
```

### 运行容器

```bash
docker run -d -p 5000:5000 clash-converter
```

启动后访问 `http://localhost:5000` 查看服务是否正常。

### 配置前端 API 地址

前端页面会从 `VITE_API_BASE_URL` 环境变量读取后端 API 地址，若未设置则默认
请求当前域名下的 `/api` 路径。在开发模式下可指定该变量：

```bash
VITE_API_BASE_URL=http://localhost:5000/api pnpm dev
```

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目：

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) - 提供高质量的分流规则集
- [Clash](https://github.com/Dreamacro/clash) - 优秀的代理工具
- 所有为开源社区做出贡献的开发者们

## 📞 支持

如果您在使用过程中遇到问题，请：

1. 查看本文档的常见问题部分
2. 搜索已有的 [Issues](https://github.com/your-repo/issues)
3. 创建新的 Issue 并提供详细信息

---

**注意**: 本工具仅供学习和研究使用，请遵守当地法律法规。
