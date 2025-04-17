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

request = iop.IopRequest('aliexpress.ds.freight.query')
request.add_api_param('queryDeliveryReq', '{\"quantity\":\"1\",\"shipToCountry\":\"FR\",\"productId\":\"3256802900954148\",\"provinceCode\":\"provice\",\"cityCode\":\"city\",\"selectedSkuId\":\"12000023999200390\",\"language\":\"en_US\",\"currency\":\"USD\",\"locale\":\"zh_CN\"}')
response = client.execute(request, access_token)

print(response.type)
print(response.body)

