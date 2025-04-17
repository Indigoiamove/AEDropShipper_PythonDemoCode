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
request = iop.IopRequest('aliexpress.ds.order.create')
request.add_api_param('ds_extend_request', '{\"payment\":{\"try_to_pay\":\"false\",\"pay_currency\":\"USD\"},\"promotion\":{\"promotion_code\":\"testCode\",\"promotion_channel_info\":\"promotionChannelInfo\"}}')
request.add_api_param('param_place_order_request4_open_api_d_t_o', '{\"product_items\":[{\"logistics_service_name\":\"EPAM\",\"sku_attr\":\"14:70221\",\"product_count\":\"2\",\"product_id\":\"1223211\",\"order_memo\":\"Please put it in a gift box.\"},{\"logistics_service_name\":\"EPAM\",\"sku_attr\":\"14:70221\",\"product_count\":\"2\",\"product_id\":\"1223211\",\"order_memo\":\"Please put it in a gift box.\"}],\"logistics_address\":{\"zip\":\"12222\",\"rut_no\":\"123-K\",\"country\":\"RU\",\"address\":\"sh Kashirskoe dom 142 (QIWI)\",\"passport_no_date\":\"02-23-2018\",\"address2\":\"sh Kashirskoe dom 142 (QIWI)\",\"city\":\"Mosco\",\"contact_person\":\"RU  TEST TEST\",\"mobile_no\":\"12334445\",\"passport_no\":\"12345\",\"locale\":\"en_US\",\"foreigner_passport_no\":\"123456789\",\"location_tree_address_id\":\"903200190000000000-903200190137000000\",\"full_name\":\"RU  TEST TEST\",\"province\":\"Mosco\",\"is_foreigner\":\"true\",\"tax_number\":\"xxx\",\"tax_company\":\"Soceite General\",\"cpf\":\"111\",\"passport_organization\":\"xxxx\",\"phone_country\":\"+7\",\"vat_no\":\"123456778\"},\"out_order_id\":\"123456789\"}')

response = client.execute(request, access_token)

print(response.type)
print(response.body)

