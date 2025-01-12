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
        # 添加默认分类
        default_categories = [
            {
                'name': '学习指导',
                'description': '学习方法、考试技巧等学习相关指导',
                'icon': 'book'
            },
            {
                'name': '生活指导',
                'description': '心理咨询、生活适应等日常生活指导',
                'icon': 'heart'
            },
            {
                'name': '职业规划',
                'description': '就业指导、考研建议等职业发展规划',
                'icon': 'compass'
            },
            {
                'name': '校园事务',
                'description': '规章制度、奖助学金等校园相关事务',
                'icon': 'bank'
            }
        ]
        
        for item in test_items:
            db.session.add(item)
        
        db.session.commit()
        print('测试数据已添加到数据库')

if __name__ == '__main__':
    init_db()
