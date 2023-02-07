import re

# # findall方法，返回匹配的结果列表
# rs = re.findall('\d+', 'chuan13adg24')
#
# # findall方法中， flag参数的作用
# re = re.findall('a.bc', 'a\nbc', re.DOTALL)   # 后面re.DOTALL能让.判断换行符
# re = re.findall('a.bc', 'a\nbc', re.S)   # 后面re.DOTALL能让.判断换行符
# print(re)

# findall方法中分组的使用
re = re.findall('a.+bc', 'a\nbc', re.DOTALL)
re = re.findall('a(.+)bc', 'a\nbc', re.DOTALL)   # ()负责定位，只会反馈（）里面的
print(re)
