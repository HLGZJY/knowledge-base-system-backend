import requests
import json
import sys

# 设置控制台输出编码为UTF-8
sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = 'http://localhost:3001/api'

def test_api():
    # 测试获取所有知识条目
    print("\n1. 测试获取所有知识条目")
    response = requests.get(f'{BASE_URL}/knowledge')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("Response:", json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print("Error:", response.text)

    # 测试搜索功能
    print("\n2. 测试搜索功能")
    response = requests.get(f'{BASE_URL}/knowledge/search', params={'q': 'Python'})
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("Response:", json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print("Error:", response.text)

if __name__ == '__main__':
    test_api()
