import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.umei.cc/katongdongman/dongmanbizhi/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find('div', class_='item_list infinite_scroll').find_all('a')
child = []
for a in alist:
    link = 'https://www.umei.cc' + a.get('href')
    child.append(link)
links = list(set(child))
for i in links:
    child_url = i
    child_resp = requests.get(child_url, headers=headers)
    child_resp.encoding = 'utf-8'
    child_page = BeautifulSoup(child_resp.text, 'html.parser')
    child_div = child_page.find('div', class_='big-pic')
    child_img = child_div.find('img')
    child_src = child_img.get('src')
    img_name = child_img.get('alt')
    img_resp = requests.get(child_src)
    # img_resp.content
    with open("img/"+img_name + '.jpg', 'wb') as f:
        f.write(img_resp.content)
    print('完成下载', img_name)
    time.sleep(1)
print("全部完成")



