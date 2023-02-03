import re
import requests

domain = 'https://www.dytt89.com/'
resp = requests.get(domain, verify=False)
resp.encoding = 'gb2312'
# print(resp.text)

obj1 = re.compile(r"2023必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<li><a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style='
                  r'"WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for i in result1:
    ul = i.group('ul')

    result2 = obj2.finditer(ul)
    for ii in result2:
        child_href = domain + ii.group('href').strip('/')
        child_href_list.append(child_href)

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    result3 = obj3.search(child_resp.text)
    movie = result3.group("movie")
    download = result3.group("download")
    print(movie)
    print(download)

    # result3 = obj3.finditer(child_resp.text)

    # for iii in result3:
    #     print(iii.group('movie'))





