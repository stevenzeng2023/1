# 导入模块
from bs4 import BeautifulSoup

# 准备文本字符串
html = '''

'''
# 创建beautifulsoup对象
soup = BeautifulSoup(html, 'lxml')
# 查找title标签
title = soup.find('title')
# 查找a标签
a = soup.find('a')
# 查找所有a标签
a_s = soup.find_all('a')


# 根据属性进行查找
# 查找ID为link的标签
a = soup.find(id='link1')   # 第一种方式，通过命名参数进行指定
a = soup.find(attrs={'id': 'link1'})  # 第二种方式，通过attrs来指定属性字典，进行查找

# 根据文本内容进行查找
text = soup.find(text='Elsie')
