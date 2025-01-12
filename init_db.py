from app import create_app
from models import db, KnowledgeItem, Category

def init_db():
    app = create_app()
    with app.app_context():
        # 删除所有表
        db.drop_all()
        # 创建所有表
        db.create_all()

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

        # 添加分类
        for category in default_categories:
            cat = Category(
                name=category['name'],
                description=category['description'],
                icon=category['icon']
            )
            db.session.add(cat)
        
        # 提交分类
        db.session.commit()

        # 添加测试数据
        test_items = [
            KnowledgeItem(
                title='测试知识条目1',
                content='这是一个测试知识条目的内容。',
                image_url='https://picsum.photos/400/200'
            ),
            KnowledgeItem(
                title='测试知识条目2',
                content='这是另一个测试知识条目的内容。',
                image_url='https://picsum.photos/400/201'
            ),
            KnowledgeItem(
                title='测试知识条目3',
                content='这是第三个测试知识条目的内容。',
                image_url='https://picsum.photos/400/202'
            )
        ]
        
        # 获取第一个分类的ID
        first_category = Category.query.first()
        if first_category:
            # 为测试数据添加分类ID
            for item in test_items:
                item.category_id = first_category.id
                db.session.add(item)
        
        db.session.commit()
        print('测试数据已添加到数据库')

if __name__ == '__main__':
    init_db()
