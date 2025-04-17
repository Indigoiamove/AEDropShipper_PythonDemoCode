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
request = iop.IopRequest('aliexpress.ds.feed.itemids.get')
request.addApiParameter("country", "CA");
request.addApiParameter("target_currency", "USD");
request.addApiParameter("target_language", "EN");
request.addApiParameter("page_size", "50");
request.addApiParameter("sort", "priceAsc");
request.addApiParameter("page_no", "1");
request.addApiParameter("category_id", "21");
request.addApiParameter("feed_name", "DS bestseller");
response = client.execute(request, access_token)

print(response.type)
print(response.body)

