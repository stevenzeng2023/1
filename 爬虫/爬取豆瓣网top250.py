import os

import requests
import re
import csv

nums = list(range(0, 250, 25))

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">'
                 r'(?P<movie>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?<span'
                 r' class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<comment>.*?)人评价</span>', re.S)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

file = os.getcwd()
if not os.path.exists(file + '\\' + 'info.csv'):
    f = open(file + '\\' + 'info.csv', 'w', newline='')
    csvwriter = csv.writer(f)
    csvwriter.writerow(['片名', '年份', '评分', '评论数'])
    urls = []
    for num in nums:
        url = f'https://movie.douban.com/top250?start={num}&filter='
        urls.append(url)
    # print(urls)
    for url in urls:
        resp = requests.get(url, headers=headers)
        result = obj.finditer(resp.text)
        for i in result:
            dic = i.groupdict()
            dic['year'] = dic['year'].strip()
            csvwriter.writerow(dic.values())
    f.close()
    print('over')

    #
#
#
#
