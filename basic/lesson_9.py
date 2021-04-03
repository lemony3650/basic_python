# 拿json数据
# from __future__ import (absolute_import, division, print_function, unicode_literals)
from urllib.request import urlopen  # 1

import json
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)  # 2
# 读取数据
req = response.read()
# 将数据写入文件
with open('text_file/btc_close_2017_urllib.json', 'wb') as f:  # 3
    f.write(req)
# 加载json格式
file_urllib = json.loads(req.decode('utf8'))  # 4
print(file_urllib)


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)  # 1
# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)  # 2
file_requests = req.json()  # 3

print(file_urllib == file_requests)
