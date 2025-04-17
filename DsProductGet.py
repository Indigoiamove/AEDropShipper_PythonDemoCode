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

request = iop.IopRequest('aliexpress.ds.product.get')
request.add_api_param('ship_to_country', 'US')
request.add_api_param('product_id', '1005007234419114')
request.add_api_param('target_currency', 'USD')
request.add_api_param('remove_personal_benefit', 'true')
request.add_api_param('target_language', 'en')
request.add_api_param('remove_personal_benefit', 'false')
response = client.execute(request, access_token)

print(response.type)
print(response.body)

