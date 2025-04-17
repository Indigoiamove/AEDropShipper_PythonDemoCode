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

request = iop.IopRequest('aliexpress.trade.ds.order.get')
request.add_api_param('single_order_query', '{\"order_id\":\"10000001\"}')
response = client.execute(request, access_token)

print(response.type)
print(response.body)

