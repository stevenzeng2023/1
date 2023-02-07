# 导入正则模块
import re
# 字符匹配
rs = re.findall('abc', 'abc')
rs = re.findall('a.c', 'abc')
rs = re.findall('a\.c', 'a.c')
rs = re.findall('a[bc]d', 'abd')

# 预定义的字符集
rs = re.findall('\d', '123')
rs = re.findall('\w', 'Az123_中文￥%')
# 数量词
rs = re.findall('a\d*', 'a123')
rs = re.findall('a\d+', 'a123')
rs = re.findall('a\d?', 'a123')
rs = re.findall('a\d{2}', 'a123')
print(rs)