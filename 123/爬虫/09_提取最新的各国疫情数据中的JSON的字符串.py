# 导入模块
import urllib.request

import requests
from bs4 import BeautifulSoup

# 发送请求，获取首页内容
response = requests.get('https://www.tianditu.gov.cn/coronavirusmap/')
urllib.request.urlretrieve()
home_page = response.content.decode()
print(home_page)
# 使用beautifulsoup提取疫情数据
# soup = BeautifulSoup(home_page, 'lxml')
# script = soup.find(id='getAreaStat')
# text = script.text
# print(text)