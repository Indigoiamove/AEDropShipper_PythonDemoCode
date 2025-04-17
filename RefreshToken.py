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
client = iop.IopClient(url, appkey ,appSecret)
request = iop.IopRequest('/auth/token/security/refresh')
request.add_api_param('refresh_token', '50001600212wcwiOabwyjtEH11acc19aBOvQr9ZYkYDlr987D8BB88LIB8bj')
response = client.execute(request)
print(response.type)
print(response.body)