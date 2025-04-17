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

client = IopClient(url, appkey, appSecret)


request = iop.IopRequest('aliexpress.ds.member.benefit.get')
#The API does not have any parameters.
response = client.execute(request, access_token)

print(response.type)
print(response.body)

