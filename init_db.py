from app import create_app
from models import db, KnowledgeItem

def init_db():
    app = create_app()
    with app.app_context():
        # 删除所有现有数据
        db.drop_all()
        # 创建所有表
        db.create_all()
        
        # 添加测试数据
        test_items = [
            KnowledgeItem(
                title='Python Programming',
                content='Python is a high-level programming language known for its simplicity and readability.',
                author_id=1,
                image_url='https://picsum.photos/400/200'
            ),
            KnowledgeItem(
                title='Flask Web Framework',
                content='Flask is a lightweight web application framework designed to get started quickly and easily.',
                author_id=1,
                image_url='https://picsum.photos/400/201'
            ),
            KnowledgeItem(
                title='React Frontend Library',
                content='React is a JavaScript library for building user interfaces, maintained by Facebook.',
                author_id=1,
                image_url='https://picsum.photos/400/202'
            )
        ]
        
        for item in test_items:
            db.session.add(item)
        
        db.session.commit()
        print('测试数据已添加到数据库')

if __name__ == '__main__':
    init_db()
