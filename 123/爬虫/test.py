import os

import requests
import re
import csv
import pandas as pd

# 源代码

new = os.getcwd() + '\\cache\\'
if not os.path.exists(new):
    os.makedirs(new)
x = new + '123' + '.csv'

num = range(0, 250, 25)
list(num)
f = open(x, 'w')
csvwriter = csv.writer(f)
for nu in num:
    url = f"https://movie.douban.com/top250?start={nu}&filter="

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'

    }
    resp = requests.get(url, headers=headers)
    page_contect = resp.text
    # print(page_contect)
    # 提取信息
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class'
                     r'="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                     r'<span>(?P<num>.*?)人评价</span>', re.S)
    result = obj.finditer(page_contect)

    for it in result:
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
f.close()
print('over')
# print(it.group('name'))
# print(it.group('score'))
# print(it.group('num'))
# print(it.group('year').strip())
