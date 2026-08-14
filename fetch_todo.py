import json
import ssl
from urllib.request import urlopen

import certifi


def fetch_json(url):
    """请求一个 URL，并把 JSON 响应转换成 Python 字典。"""
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    with urlopen(url, timeout=5, context=ssl_context) as response:
        if response.status != 200:
            raise RuntimeError(f"请求失败，状态码：{response.status}")
        return json.load(response)


if __name__ == "__main__":
    todo = fetch_json("https://jsonplaceholder.typicode.com/todos/1")
    print(f"任务：{todo['title']}")
    print(f"是否完成：{todo['completed']}")
