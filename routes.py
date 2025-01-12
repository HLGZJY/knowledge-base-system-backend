from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from models import db, KnowledgeItem

api = Blueprint('api', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@api.route('/knowledge', methods=['GET'])
def get_knowledge_items():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search = request.args.get('q', '')

    query = KnowledgeItem.query
    if search:
        query = query.filter(
            db.or_(
                KnowledgeItem.title.ilike(f'%{search}%'),
                KnowledgeItem.content.ilike(f'%{search}%')
            )
        )
    
    items = query.order_by(KnowledgeItem.created_at.desc()).all()
    return jsonify({
        'data': [item.to_dict() for item in items],
        'total': len(items),
        'page': page,
        'per_page': per_page
    })

@api.route('/knowledge/<int:id>', methods=['GET'])
def get_knowledge_item(id):
    item = KnowledgeItem.query.get_or_404(id)
    return jsonify(item.to_dict())

@api.route('/knowledge', methods=['POST'])
def create_knowledge_item():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json()
    if not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Title and content are required'}), 400

    item = KnowledgeItem.from_dict(data)
    db.session.add(item)
    db.session.commit()
    
    return jsonify(item.to_dict()), 201

@api.route('/knowledge/<int:id>', methods=['PUT'])
def update_knowledge_item(id):
    item = KnowledgeItem.query.get_or_404(id)
    
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json()
    
    if 'title' in data:
        item.title = data['title']
    if 'content' in data:
        item.content = data['content']
    if 'imageUrl' in data:
        item.image_url = data['imageUrl']
    
    db.session.commit()
    return jsonify(item.to_dict())

@api.route('/knowledge/<int:id>', methods=['DELETE'])
def delete_knowledge_item(id):
    item = KnowledgeItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

@api.route('/knowledge/search', methods=['GET'])
def search_knowledge():
    keyword = request.args.get('q', '')
    if not keyword:
        return get_knowledge_items()

    items = KnowledgeItem.query.filter(
        db.or_(
            KnowledgeItem.title.ilike(f'%{keyword}%'),
            KnowledgeItem.content.ilike(f'%{keyword}%')
        )
    ).all()

    return jsonify({
        'data': [item.to_dict() for item in items],
        'total': len(items)
    })

@api.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # 生成唯一文件名
        unique_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename))
        
        # 返回文件URL
        file_url = f"/uploads/{unique_filename}"
        return jsonify({'url': file_url})
# 获取所有分类
@api.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([cat.to_dict() for cat in categories])

# 根据分类获取知识条目
@api.route('/knowledge/category/<int:category_id>', methods=['GET'])
def get_knowledge_by_category(category_id):
    items = KnowledgeItem.query.filter_by(category_id=category_id).all()
    return jsonify([item.to_dict() for item in items])