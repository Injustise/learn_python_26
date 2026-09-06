import requests

try:
    resp = requests.get("https://apis.tianapi.com/guonei/index?key=f22b78988d51754aa8b09e0018b9192f&num=3")
    if resp.status_code == 200:
        data_model = resp.json()

        if(data_model.get('code') == 200):
            print('-' * 64)
            for news in data_model.get('result', {}).get('newslist', []):
                print(news['title'], end = ' ')
                print(f"({news['ctime']})")
                print(news['url'])
                print('-' * 64)
        else:
            print(f"API 报错：{data_model.get('msg')}")
except Exception as err:
    print(f"请求失败{err}")