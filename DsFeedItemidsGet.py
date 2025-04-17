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
request = iop.IopRequest('aliexpress.ds.recommend.feed.get')

request.addApiParameter("page_size", "200");
request.addApiParameter("feed_name", "DS bestseller");
request.addApiParameter("search_id", "abc123");
response = client.execute(request, access_token)

print(response.type)
print(response.body)

