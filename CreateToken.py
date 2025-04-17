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
request = iop.IopRequest('/auth/token/create')
request.add_api_param('code', '0_2DL4DV3jcU1UOT7WGI1A4rY91')
response = client.execute(request)
print(response.type)
print(response.body)