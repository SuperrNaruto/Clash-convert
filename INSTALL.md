# Clash订阅转换程序 v2.0 安装说明

## 📋 系统要求

- Python 3.7+
- Node.js 16+ (用于Web版本)
- 操作系统: Windows/macOS/Linux

## 🚀 快速开始

### 1. 命令行版本

```bash
# 安装Python依赖
pip install -r requirements.txt

# 运行示例
python example.py

# 或直接使用主程序
python main.py
```

### 2. Web版本部署

#### 后端API部署
```bash
cd clash-converter-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

#### 前端应用部署
```bash
cd clash-converter-web
npm install
npm run build
npm run preview
```

## 🌐 在线版本

- **前端应用**: https://ztvxjxgs.manus.space
- **后端API**: https://60h5imceeqy0.manus.space

## 📖 使用说明

详细使用说明请参考:
- `README.md` - 项目概述和功能介绍
- `使用说明.md` - 详细使用指南
- `design_doc.md` - 设计文档

## 🔧 配置说明

主要配置文件:
- `config.py` - 核心配置
- `templates/` - 策略组模板
- `rules/` - 规则文件

## 🆘 问题排查

1. **依赖安装失败**: 确保Python和pip版本正确
2. **网络连接问题**: 检查防火墙和代理设置
3. **规则集获取失败**: 可能是网络问题，程序会自动重试

## 📄 许可证

MIT License - 详见 LICENSE 文件
