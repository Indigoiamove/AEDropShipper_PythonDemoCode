
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
client = iop.IopClient(url, appkey ,appSecret)
request = iop.IopRequest('aliexpress.ds.image.searchV2''POST')
request.add_api_param('param0', '{\"sort_type\":\"price\",\"image_base64\":\"imageBase64\",\"currency\":\"USD\",\"lang\":\"en\",\"search_type\":\"same\",\"sort_order\":\"asc\",\"ship_to\":\"US\"}')
response = client.execute(request, access_token)
print(response.type)
print(response.body)