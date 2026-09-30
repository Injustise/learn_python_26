import requests

try:
    # 通过 requests 模块的 get 函数向天聚数行的国内新闻接口发起了一次请求，并获取一个 Response 对象
    resp = requests.get("https://apis.tianapi.com/guonei/index?key=f22b78988d51754aa8b09e0018b9192f&num=5") # num 表示返回的数据个数数
    if resp.status_code == 200: # HTTP 状态码，请求是否到达服务器（服务器层面）
        data_model = resp.json() # json() 可以将返回的 JSON 格式的数据直接处理成 Python 字典

        if(data_model.get('code') == 200): # 业务状态码，业务是否处理成功（业务层面：API-Key 正确与否，额度足够与否，请求参数合法与否）
            print('-' * 64)
            for news in data_model.get('result', {}).get('newslist', []): # get() 可以避免 [] 索引不存在时报错：KeyError
                print(news['title'], end = ' ')
                print(f"({news['ctime']})")
                print(news['url'])
                print('-' * 64)
        else:
            print(f"API 报错：{data_model.get('msg')}")
except Exception as err:
    print(f"请求失败{err}")