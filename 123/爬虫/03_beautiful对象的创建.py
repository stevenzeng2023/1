# 导入模块
from bs4 import BeautifulSoup
# 创建beautifulsoup对象
soup = BeautifulSoup('<html>data</html>', 'lxml')
print(soup)