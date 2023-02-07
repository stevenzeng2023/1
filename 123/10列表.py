"""
list列表的循环，使用while和 for循环2种方式
"""

# def list_while_func():
#     """
#     使用while循环
#     :return: None
#     """
#     my_list = ["I", "have", "a", "little", "dog"]
#     # 循环控制变量，使用下标索引可控制，默认0
#     # 每一次循环将下标索引变量+1
#     # 循环条件：下标索引变量 < 列表的元素数量
#
#     # 定义一个变量用来标记列表的下标
#     index = 0
#     while index < len(my_list):
#         element = my_list[index]
#         print(f"列表的元素：{element}")
#         index += 1
#
#
#
#
# def list_for_func():
#     my_list = [1, 2, 3, 4, 5]
#     for element in my_list:
#         print(f"列表的元素：{element}")
#
# list_while_func()
# list_for_func()


# 取出列表内的偶数
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def list_while():
#     index = 0
#     global my_list
#     while index < len(my_list):
#         index += 1
#         element = my_list[index]
#         if element % 2 == 0:
#             print(f"偶数：{element}")


# def list_for():
#     global my_list
#     for element in my_list:
#         if element % 2 == 0:
#             print(f"偶数：{element}")


# list_while()
# list_for()


# # 元组 不可修改，例子
# my_list = ('张三', 15, ['music', 'game'])
# index = my_list.index(15)
# print(f"年龄所在的下标位置：{index}")
# name = my_list[0]
# print(f"姓名：{name}")
# del my_list[2][1]
# print(f"删除爱好game：{my_list}")


# # replace 方法
# my_str = "I have a little dog"
# new_my_str = my_str.replace("little", "big")
# print(f"将字符串{my_str},进行替换后得到的：{new_my_str}")

# split 方法
# my_str = "I have a little dog"
# my_str_list = my_str.split(" ")   # 按照什么来切分，这里是按照空格来切分
# print(f"将字符串{my_str}, 进行split切分后得到：{my_str_list}, 类型是：{type(my_str_list)}")


# strip 规整操作
# my_str = "  I have a little dog  "
# new_my_str = my_str.strip()  # 不传入参数， 取出首尾空格
# print(f"字符串{my_str}被strip后， 结果：{new_my_str}")
#
# my_str = "12I have a little dog21"
# new_my_str = my_str.strip("12")
# print(f"字符串{my_str}被strip('12')后， 结果：{new_my_str}")


# # 统计字符串中牟字符串的出现次数，count
# my_str = "I have a little dog"
# count = my_str.count("a")
# print(f"字符串{my_str}中a出现的次数：{count}次")
#
# # 统计字符串的长度
# my_str = "I have a little dog"
# num = len(my_str)
# print(f"字符串{my_str}的长度是{num}")

# # 字符串的遍历
# my_str = "dog"
# index = 0
# while index < len(my_str):  # while 方法
#     print(my_str[index])
#     index += 1
#
# for i in my_str:
#     print(i)


# # 练习分割字符串
# my_str = "the lucky dog is very lucky"
# num = my_str.count('lucky')
# print(f"字符串内有'lucky'{num}个")
# new_my_str = my_str.replace(" ", "|")
# print(f"将字符串的空格全部替换成'|'字符:{new_my_str}")
# my_list = new_my_str.split('|')
# print(f"按照'|'进行字符串分给，得到列表{my_list}")
