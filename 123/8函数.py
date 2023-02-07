# 统计字符串的长度
# str1 = "adfgsaggh"
# str2 = "452138853"
# str3 = "^%&**(("
#
# count = 0
# for i in str1:
#      count += 1
# print(f"字符串的{str1}的长度是：{count}")

# 使用函数来统计
# str1 = "adfgsaggh"
# str2 = "452138853"
# str3 = "^%&**(("
#
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串的{str1}的长度是：{count}")
# my_len(str1)
# my_len(str2)
# my_len(str3)

# 定义函数
# def say_hi():
#     print("hi,hello")
# # 调用函数
# say_hi()

#
#  自动查核酸  \n 换行
# def check():
#     print("欢迎来到xxxx！\n请出示您的健康码以及48小时核酸证明！")
# check()


# 函数的传入参数
# def add(x, y, z):
#     result = x + y + z
#     print(f"{x} + {y} + {z}的计算结果： {result}")
# add(1, 3, 4)

# 升级版的自动查核酸
# def check(temperature):
#     print("欢迎来到我家，请提供您的体温！")
#     if temperature <= 37.5:
#         print(f"您的体温是：{temperature},体温正常，请进！")
#     else:
#         print(f"您的体温是：{temperature},需要隔离！")
# check(float(input("请输入您的体温：")))


# 返回值的简单应用
# def add(a, b):
#     """
#     函数的说明文档
#     :param a:
#     :param b:
#     :return:
#     """
#     result = a + b
#     return result
# r = add(5, 6)
# print(r)

# None的应用 if的判断
# num = int(input("请输入年龄："))
# def  check_age (age):
#     if age >= 18:
#         print("认证成功，请进！")
#         return "SUCCESS"
# result = check_age(num)
# if not result:
#     print("未成年人，不可进入！")

# 嵌套调用函数
# def func_b():
#     print("--2--")
# def func_a():
#     print("--1--")
#     func_b()
#     print("--3--")
# func_a()

# 局部变量
# def test_a():
#     num = 100
#     print(num)
# test_a()
# print(num)

# global修改为全局变量
# def test_a():
#     global num
#     num = 100
#     print(num)
# test_a()
# print(num)

# # 演示函数综合案例开发
# money = 50000000
#
# name = input("请输入您的姓名：")
#
# def query(show_header):
#     if show_header:
#         print("---------查询余额----------")
#     print(f"{name}，您好，您的余额剩余：{money}元")
# def saving(num):
#     global money
#     money += num
#     print("---------存款----------")
#     print(f"{name}，您好，您存款{num}元成功")
#     query(False)
#
# def get_money(num):
#     global money
#     money -= num
#     print("---------取款----------")
#     print(f"{name}，您好，您取款{num}元成功。")
#     query(False)
#
# def main():
#     print("---------主菜单----------")
#     print(f"{name}，您好，欢迎来到xx银行ATM，请选择操作：")
#     print("查询余额 \t[输入1]")
#     print("存款 \t\t[输入2]")
#     print("取款 \t\t[输入3]")
#     print("退出 \t\t[输入4]")
#     return input("请输入您的选择：")
#
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query(True)
#         continue
#     elif keyboard_input == "2":
#         num = int(input("您想存多少钱？请输入： "))
#         saving(num)
#         continue
#     elif keyboard_input == "3":
#         num = int(input("您想取出多少钱？请输入： "))
#         get_money(num)
#         continue
#     elif keyboard_input == "4":
#         print("程序已退出。")
#         break
#     else:
#         print("请输入1-4。")


# # 多个返回值
# def test_return():
#     return 1, "hello", True
# x, y, z = test_return()            # 位置传参
# print(x, y, z)

# # 关键字传参  可与位置传参混用，位置传参优先放前面
# def user_info (name, age, gender='男'):   # 缺省值必须在最后面
#     print(f"姓名：{name}， 年龄：{age}， 性别：{gender}")
# user_info('张三', 20, '男')     # 位置传参
# user_info(name='李四', age=21)    # 关键字传参、缺省值参数
# user_info('王八', gender='男', age=22)    # 关键字传参
# user_info('宋小', gender='女', age=18)    # 缺省参数可修改


# # 位置不定长传参 *号
# def user_info(*args):
#     print(f"args参数类型是：{type(args)}, 内容是：{args}")   # 元组形式
#
# user_info(1, 2, 3, '小米', '女')
#
#
# # 关键字不定长传参 **号
# def user_info(**kwargs):
#     print(f"args参数类型是：{type(kwargs)}, 内容是：{kwargs}")   # dict形式
#
# user_info(name='小米', age=18, gender='女孩', addr='珠海')


# 匿名函数
def test_func(compute):
    result = compute(1, 2)
    print(f"结果：{result}")
def compute(x, y):
    return x + y

test_func(compute)  # 函数调用函数

test_func(lambda x, y: x + y)  # 匿名函数的应用方法

