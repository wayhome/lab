# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
#     "rich",
# ]
# ///

## 使用 uv 添加脚本 inline 依赖
## uv add --script example.py  'rich' 'requests'
## 使用 uv 运行
## uv run example.py

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
