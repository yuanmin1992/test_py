"""
myreq.py  
模块功能:
parse_url 方法给 url 就返回 html

简单反反爬
1.随机 User-Agent
2.随机代理服务器

容错处理
1.重试
2.超时
"""

import requests
import random
from retrying import retry

# 随机 User-Agent
USER_AGENT_LIST = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15"
]

# 定义 代理服务器
# 未来 2个 代理服务器列表可能从第三方购买的
HTTP_PROXIES = [
    'http://115.223.197.119:9000',
]
HTTPS_PROXIES = [
    'https://218.60.8.99:3129'
]

@retry(stop_max_attempt_number=5)
def __parse_url(url,method='get',data={},proxies={}):
    print("***请求中***")
    headers = {
        'User-Agent': random.choice(USER_AGENT_LIST)
    }

    if method=='get':
        response = requests.get(
            url,
            headers=headers,
            proxies=proxies,
            timeout=2,
            params=data
        )
    else:
        response = requests.post(
            url,
            headers=headers,
            proxies=proxies,
            timeout=2,
            params=data
        )
    response.encoding = 'utf-8'
    return response.text


def parse_url(url, method='get', data={}):
    """
    请求并返回html内容
    :param self:
    :param url:
    :return:
    """
    html = None
    proxies = {
        "http": random.choice(HTTP_PROXIES) if len(HTTP_PROXIES) > 0 else None,
        "https": random.choice(HTTPS_PROXIES) if len(HTTPS_PROXIES) > 0 else None
    }

    try:
        html = __parse_url(url,method=method,proxies=proxies,data=data)
    except:
        # 加点log日志
        html = None

    # 删除无效的代理
    if html is None:
        scheme = requests.utils.urlparse(url).scheme
        if scheme == 'http':
            print("当前代理无效:",proxies['http'])
            HTTP_PROXIES.remove(proxies['http'])
        elif scheme == 'https':
            print("当前代理无效:", proxies['https'])
            HTTPS_PROXIES.remove(proxies["https"])
    # print(HTTP_PROXIES)
    # print(HTTPS_PROXIES)
    return html

if __name__ == '__main__':
    print(parse_url("https://www.baidu.com"))
