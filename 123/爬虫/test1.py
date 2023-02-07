# 1.定位
# 2.提取子页面地址
# 3.请求子页面的连接地址，拿到下载地址
import re
import requests
domain = 'https://www.dytt89.com/'
resp = requests.get(domain, verify=False)  # verify=False 去掉安全验证
resp.encoding = 'gb2312'
# print(resp.text)
obj1 = re.compile(r'2023必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style='
                  r'"WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')
    result2 = obj2.finditer(ul)
    for itt in result2:
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href)
        # print(child_href)

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    result3 = obj3.search(child_resp.text)
    print(result3.group('movie'))
    print(result3.group('download'))


