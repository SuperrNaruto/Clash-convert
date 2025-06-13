# Clash订阅转换程序设计文档

## 1. 项目概述

本项目旨在创建一个Clash订阅转换程序，可以将订阅链接转换为具有完整精细分流规则的配置文件，包括多个策略组和去广告规则。

## 2. 功能需求

1. 获取并解析订阅链接内容
2. 添加自定义策略组（YouTube等流媒体组，Telegram, Instagram, Twitter, Bilibili, ChatGPT和Claude等AI策略组）
3. 添加精细分流规则
4. 添加去广告规则
5. 生成完整的Clash配置文件

## 3. 系统架构

程序将采用模块化设计，主要包含以下组件：

1. **订阅获取模块**：负责从URL获取原始订阅内容
2. **订阅解析模块**：解析原始订阅内容，提取节点信息
3. **策略组生成模块**：根据预设模板生成各类策略组
4. **规则集获取模块**：获取和管理各类分流规则集
5. **配置生成模块**：整合节点、策略组和规则，生成最终配置文件

## 4. 模块设计

### 4.1 订阅获取模块

- 功能：从URL获取原始订阅内容
- 输入：订阅链接URL
- 输出：原始订阅内容（Base64编码或YAML格式）
- 主要方法：
  - `fetch_subscription(url)`: 获取订阅内容
  - `validate_subscription(content)`: 验证订阅内容有效性

### 4.2 订阅解析模块

- 功能：解析原始订阅内容，提取节点信息
- 输入：原始订阅内容
- 输出：标准化的节点列表
- 主要方法：
  - `parse_subscription(content)`: 解析订阅内容
  - `convert_to_clash_nodes(nodes)`: 将节点转换为Clash格式

### 4.3 策略组生成模块

- 功能：根据预设模板生成各类策略组
- 输入：节点列表，策略组模板
- 输出：Clash格式的策略组配置
- 主要方法：
  - `generate_proxy_groups(nodes, templates)`: 生成策略组
  - `create_group_by_type(group_type, nodes)`: 根据类型创建特定策略组

### 4.4 规则集获取模块

- 功能：获取和管理各类分流规则集
- 输入：规则集URL或本地文件路径
- 输出：规则集内容
- 主要方法：
  - `fetch_ruleset(source)`: 获取规则集
  - `parse_ruleset(content)`: 解析规则集内容
  - `get_adblock_rules()`: 获取去广告规则

### 4.5 配置生成模块

- 功能：整合节点、策略组和规则，生成最终配置文件
- 输入：节点列表，策略组配置，规则集
- 输出：完整的Clash配置文件
- 主要方法：
  - `generate_config(nodes, proxy_groups, rulesets)`: 生成配置文件
  - `save_config(config, path)`: 保存配置文件

## 5. 数据流

1. 用户提供订阅链接
2. 订阅获取模块获取原始订阅内容
3. 订阅解析模块解析内容并提取节点
4. 策略组生成模块根据节点生成策略组
5. 规则集获取模块获取各类规则集
6. 配置生成模块整合所有内容，生成最终配置文件
7. 将配置文件返回给用户

## 6. 技术选型

- 编程语言：Python 3
- 主要依赖库：
  - requests：用于HTTP请求
  - pyyaml：用于YAML格式处理
  - base64：用于Base64编码/解码
  - re：用于正则表达式处理

## 7. 文件结构

```
clash_sub_converter/
├── main.py                  # 主程序入口
├── config.py                # 配置文件
├── modules/
│   ├── __init__.py
│   ├── subscription.py      # 订阅获取和解析模块
│   ├── proxy_groups.py      # 策略组生成模块
│   ├── rulesets.py          # 规则集获取模块
│   └── generator.py         # 配置生成模块
├── templates/
│   ├── groups/              # 策略组模板
│   │   ├── streaming.yaml   # 流媒体策略组模板
│   │   ├── social.yaml      # 社交媒体策略组模板
│   │   └── ai.yaml          # AI服务策略组模板
│   └── config.yaml          # 基础配置模板
└── rules/                   # 本地规则集
    ├── adblock.list         # 去广告规则
    ├── streaming.list       # 流媒体规则
    ├── social.list          # 社交媒体规则
    └── ai.list              # AI服务规则
```

## 8. 实现计划

1. 创建基本项目结构和文件
2. 实现订阅获取和解析模块
3. 实现策略组生成模块
4. 实现规则集获取模块
5. 实现配置生成模块
6. 整合所有模块，完成主程序
7. 测试和优化
8. 编写使用文档

## 9. 预期成果

一个功能完整的Clash订阅转换程序，可以将普通订阅链接转换为具有完整精细分流规则的配置文件，包括多个策略组和去广告规则。用户可以通过简单的命令行操作完成转换过程。

