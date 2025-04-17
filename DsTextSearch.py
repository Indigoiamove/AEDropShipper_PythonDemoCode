import sys
import iop
sys.path.append('./python')
from iop import base
from iop.base import *
from iop.base import IopClient
from iop.base import IopRequest

#instance = IopClient(url, appkey, appSecret)
url = "https://api-sg.aliexpress.com/sync"
appkey = ""
appSecret = ""
access_token = "";
# 创建客户端实例
client = IopClient(url, appkey, appSecret)
# 创建请求实例

request = iop.IopRequest('aliexpress.ds.text.search')
request.add_api_param('keyWord', '\u88D9\u5B50')
request.add_api_param('local', 'zh_CN')
request.add_api_param('countryCode', 'US')
request.add_api_param('categoryId', '349')
request.add_api_param('sortBy', 'min_price,asc')
request.add_api_param('pageSize', '20')
request.add_api_param('pageIndex', '1')
request.add_api_param('currency', 'USD')
response = client.execute(request, access_token)

print(response.type)
print(response.body)

