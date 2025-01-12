import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_migrate import Migrate
from models import db
from routes import api
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # 配置
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')
    app.config['JSON_AS_ASCII'] = False  # 确保JSON响应可以包含非ASCII字符
    
    # 确保上传文件夹存在
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # 配置CORS，允许所有来源
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # 初始化扩展
    db.init_app(app)
    Migrate(app, db)
    
    # 注册蓝图
    app.register_blueprint(api, url_prefix='/api')
    
    # 添加静态文件路由
    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
