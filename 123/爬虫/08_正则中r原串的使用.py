import re

rs = re.findall('a\nbc', 'a\nbc')


rs = re.findall('a\\nbc', 'a\\nbc')
rs = re.findall('a\\\\nbc', 'a\\\\nbc')
rs = re.findall(r'a\\nbc', 'a\\nbc')
rs = re.findall(r'a\nbc', 'a\nbc')

# 扩展：可以解决写正则的时候，不符合pep8规范的问题
rs = re.findall(r'\d', 'a123')