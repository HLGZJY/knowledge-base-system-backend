import requests
import json
import sys

# 设置控制台输出编码为UTF-8
sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = 'http://localhost:3001/api'

def test_categories():
    print("\n1. 测试获取所有分类")
    response = requests.get(f'{BASE_URL}/categories')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        categories = response.json()
        print("分类列表:", json.dumps(categories, indent=2, ensure_ascii=False))
        # 保存第一个分类的ID用于后续测试
        if categories:
            return categories[0]['id']
    else:
        print("Error:", response.text)
    return None

def test_knowledge_by_category(category_id):
    if category_id is None:
        print("\n2. 跳过分类知识测试：没有有效的分类ID")
        return

    print(f"\n2. 测试获取分类 {category_id} 的知识条目")
    response = requests.get(f'{BASE_URL}/knowledge/category/{category_id}')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        items = response.json()
        print("该分类下的知识条目:", json.dumps(items, indent=2, ensure_ascii=False))
    else:
        print("Error:", response.text)

def test_knowledge():
    print("\n3. 测试获取所有知识条目")
    response = requests.get(f'{BASE_URL}/knowledge')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("所有知识条目:", json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print("Error:", response.text)

def test_search():
    print("\n4. 测试搜索功能")
    search_term = "测试"
    response = requests.get(f'{BASE_URL}/knowledge/search', params={'q': search_term})
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"搜索 '{search_term}' 的结果:", json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print("Error:", response.text)

def run_all_tests():
    print("开始API测试...")
    # 先测试分类API
    category_id = test_categories()
    # 使用返回的分类ID测试分类知识条目
    test_knowledge_by_category(category_id)
    # 测试其他API
    test_knowledge()
    test_search()
    print("\n测试完成!")

if __name__ == '__main__':
    run_all_tests()
