
# 算数运算符
print("1+1=", 1+1)

num = 1 + 2 * 3
num = 1
num += 1  # num = num + 1
print("num += 1:", num)


# 单引号定义法
name = '程序员'
print(type(name))
# 双引号定义法
name = "程序员"
print(type(name))
# 三引号定义法
name = """程序员"""
print(type(name))


name ='"程序员“'
print(name)
# 使用转义字符
name = "\"程序员\""
print(name)
name = '\'程序员\''
print(name)
name = '"程序员"'
print(name)

# 字符串拼接
print("我是" + "程序员")
# 字符串字面和字符串变量拼接
name = "程序员"
address = "南沙湾的"
tel = 12345566
print("我是" + address + name)

# 字符串格式化，占位
name = "程序员"
money_1 = "16000"
money_12 = "200000"
message = "月薪：%s，年薪：%s" % (money_1, money_12)
print(name + message)

#字符串精度控制
num1 = 11
num2 = 11.123
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.123宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.123不限制，小数精度2，结果是：%.2f" % num2)

# 字符串快速格式化
name = "程序员"
money_1 = 6000.1234
print(f"我是{name}，月薪只有：{money_1}元")

# 字符串表达式格式化
print("1*2的结果是：%d" % (1*2))
print(f"1*2的结果是：{1*2}")
print("字符串的类型是：%s " % type("字符串"))

