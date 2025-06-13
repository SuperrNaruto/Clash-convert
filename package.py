#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clash订阅转换程序打包脚本 v2.0

用于创建程序的发布包，包含所有必要文件和文档。
"""

import os
import shutil
import zipfile
import datetime

def create_package():
    """创建发布包"""
    
    # 版本信息
    version = "v2.0"
    date_str = datetime.datetime.now().strftime("%Y%m%d")
    package_name = f"clash_sub_converter_{version}_{date_str}"
    
    print(f"创建发布包: {package_name}")
    
    # 创建临时目录
    temp_dir = f"temp_{package_name}"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    # 要包含的文件和目录
    include_items = [
        # 主程序文件
        'main.py',
        'config.py',
        'requirements.txt',
        'example.py',
        
        # 文档文件
        'README.md',
        '使用说明.md',
        'LICENSE',
        
        # 模块目录
        'modules/',
        
        # 模板目录
        'templates/',
        
        # 规则目录（如果存在）
        'rules/',
    ]
    
    # 复制文件和目录
    for item in include_items:
        src_path = item
        dst_path = os.path.join(temp_dir, item)
        
        if os.path.exists(src_path):
            if os.path.isfile(src_path):
                # 复制文件
                shutil.copy2(src_path, dst_path)
                print(f"复制文件: {src_path}")
            elif os.path.isdir(src_path):
                # 复制目录
                shutil.copytree(src_path, dst_path)
                print(f"复制目录: {src_path}")
        else:
            print(f"警告: 文件或目录不存在: {src_path}")
    
    # 创建空的缓存目录
    cache_dir = os.path.join(temp_dir, 'cache')
    os.makedirs(cache_dir, exist_ok=True)
    
    # 创建缓存目录说明文件
    with open(os.path.join(cache_dir, 'README.txt'), 'w', encoding='utf-8') as f:
        f.write("此目录用于存储规则集缓存文件，提升程序运行速度。\n")
        f.write("缓存文件会在程序运行时自动创建。\n")
    
    # 创建版本信息文件
    version_info = f"""Clash订阅转换程序 {version}

发布日期: {datetime.datetime.now().strftime("%Y年%m月%d日")}
构建时间: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

主要特性:
- 支持10种策略组分类
- 使用blackmatrix7/ios_rule_script高质量规则集
- 智能缓存系统，提升转换速度
- 支持多种订阅格式
- 完善的错误处理机制

新增功能:
- 科技巨头策略组（Apple、Google、Microsoft、Amazon）
- 游戏服务策略组（Steam、Epic Games、PlayStation等）
- 金融服务策略组（PayPal、支付宝）
- 购物电商策略组（Amazon、淘宝、京东等）
- 新闻媒体策略组（BBC、CNN、Reuters等）
- 开发工具策略组（GitHub、GitLab、Docker等）

技术改进:
- 规则集数量从5个增加到76个
- 转换速度提升10倍以上
- 更精细的分流控制
- 更好的用户体验

使用方法:
1. 安装依赖: pip install -r requirements.txt
2. 基础使用: python main.py <订阅链接>
3. 查看帮助: python main.py --help
4. 查看示例: python example.py

更多信息请查看 README.md 和 使用说明.md 文件。
"""
    
    with open(os.path.join(temp_dir, 'VERSION.txt'), 'w', encoding='utf-8') as f:
        f.write(version_info)
    
    # 创建快速开始指南
    quick_start = """# 快速开始指南

## 1. 安装依赖
```bash
pip install -r requirements.txt
```

## 2. 查看程序信息
```bash
python main.py --info
python main.py --list-groups
```

## 3. 基础使用
```bash
# 使用默认策略组
python main.py https://your-subscription-url

# 使用所有策略组
python main.py https://your-subscription-url --all

# 自定义策略组
python main.py https://your-subscription-url --include-streaming --include-ai
```

## 4. 查看示例
```bash
python example.py
```

## 5. 获取帮助
```bash
python main.py --help
```

更多详细信息请查看 README.md 和 使用说明.md 文件。
"""
    
    with open(os.path.join(temp_dir, 'QUICKSTART.md'), 'w', encoding='utf-8') as f:
        f.write(quick_start)
    
    # 创建发布包目录
    dist_dir = 'dist'
    os.makedirs(dist_dir, exist_ok=True)
    
    # 创建ZIP文件
    zip_path = os.path.join(dist_dir, f"{package_name}.zip")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_path = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arc_path)
                print(f"添加到压缩包: {arc_path}")
    
    # 清理临时目录
    shutil.rmtree(temp_dir)
    
    # 显示结果
    file_size = os.path.getsize(zip_path)
    print(f"\n✅ 发布包创建成功!")
    print(f"文件路径: {os.path.abspath(zip_path)}")
    print(f"文件大小: {file_size / 1024:.1f} KB")
    
    # 创建发布说明
    release_notes = f"""# Clash订阅转换程序 {version} 发布说明

## 📦 发布信息
- 版本: {version}
- 发布日期: {datetime.datetime.now().strftime("%Y年%m月%d日")}
- 文件名: {package_name}.zip
- 文件大小: {file_size / 1024:.1f} KB

## 🎯 主要特性
- **10种策略组分类**: 流媒体、社交媒体、AI服务、科技巨头、游戏服务、金融服务、购物电商、新闻媒体、开发工具、广告拦截
- **76个高质量规则集**: 使用blackmatrix7/ios_rule_script仓库的规则集
- **智能缓存系统**: 规则集缓存24小时，转换速度提升10倍以上
- **多种订阅格式**: 支持Clash YAML和Base64编码订阅
- **完善错误处理**: 自动跳过不可用规则集，优雅降级

## 🆕 新增功能
### 新策略组类型
- **科技巨头** (techgiants): Apple、Google、Microsoft、Amazon服务
- **游戏服务** (gaming): Steam、Epic Games、PlayStation、Xbox等
- **金融服务** (finance): PayPal、支付宝
- **购物电商** (shopping): Amazon、淘宝、京东、eBay等
- **新闻媒体** (news): BBC、CNN、Reuters、Fox News等
- **开发工具** (developer): GitHub、GitLab、Docker、npm等

### 技术改进
- 规则集数量从5个增加到76个
- 转换速度从60-120秒优化到1-3秒（使用缓存）
- 更精细的分流控制
- 更好的命令行界面

## 🚀 使用方法
### 基础使用
```bash
# 安装依赖
pip install -r requirements.txt

# 使用默认策略组
python main.py https://your-subscription-url

# 使用所有策略组
python main.py https://your-subscription-url --all
```

### 自定义配置
```bash
# 流媒体爱好者
python main.py https://your-subscription-url --include-streaming --include-social --include-adblock

# 程序开发者
python main.py https://your-subscription-url --include-developer --include-techgiants --include-ai --include-adblock

# 游戏玩家
python main.py https://your-subscription-url --include-gaming --include-social --include-streaming --include-adblock
```

### 查看信息
```bash
# 查看规则集信息
python main.py --info

# 列出策略组类型
python main.py --list-groups

# 查看帮助
python main.py --help
```

## 📋 系统要求
- Python 3.7 或更高版本
- 网络连接（用于获取规则集）
- 约100MB磁盘空间（包含缓存）

## 📚 文档
- README.md - 英文详细说明
- 使用说明.md - 中文使用指南
- QUICKSTART.md - 快速开始指南
- example.py - 使用示例脚本

## 🐛 已知问题
- 部分规则集可能因GitHub访问问题获取失败（程序会自动跳过）
- 首次运行需要较长时间下载规则集（后续运行使用缓存）

## 🔄 升级说明
从v1.0升级到v2.0:
1. 备份现有配置和自定义规则
2. 下载新版本程序包
3. 重新安装依赖: pip install -r requirements.txt
4. 测试新功能: python main.py --info

## 📞 技术支持
- 查看文档: README.md 和 使用说明.md
- 提交Issue: 在项目仓库中报告问题
- 社区讨论: 参与项目讨论

---
感谢使用Clash订阅转换程序！
"""
    
    release_notes_path = os.path.join(dist_dir, f"RELEASE_NOTES_{version}_{date_str}.md")
    with open(release_notes_path, 'w', encoding='utf-8') as f:
        f.write(release_notes)
    
    print(f"发布说明: {os.path.abspath(release_notes_path)}")
    
    return zip_path

def main():
    """主函数"""
    print("Clash订阅转换程序打包脚本 v2.0")
    print("=" * 50)
    
    try:
        zip_path = create_package()
        print(f"\n🎉 打包完成! 发布包位置: {zip_path}")
        
    except Exception as e:
        print(f"\n❌ 打包失败: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

