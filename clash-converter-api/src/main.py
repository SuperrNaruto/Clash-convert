import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.routes.converter import converter_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# 启用CORS支持
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# 注册蓝图
app.register_blueprint(converter_bp, url_prefix='/api')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "Clash订阅转换程序 API 服务正在运行", 200


if __name__ == '__main__':
    print("🚀 Clash订阅转换程序 API 服务启动中...")
    print("📡 API端点:")
    print("   POST /api/convert - 转换订阅")
    print("   GET  /api/info - 获取程序信息")
    print("   GET  /api/groups - 获取策略组列表")
    print("   GET  /api/health - 健康检查")
    print("🌐 服务地址: http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

