# list列表
# name_list = ['it', 'python', 'cast']
# print(name_list)
# print(type(name_list))


# list 下标索引 从0开始，每次+1，反向从-1开始，每次-1
# name_list = ['Mary', 'Tom', 'Cathy']
# print(name_list[0])
# print(name_list[-1])
# print(name_list[1])

# 取出嵌套列表中的元素
# num_list = [[1, 2, 3], [4, 5, 6]]
# print(num_list[0][0])
# print(num_list[-1][-1])

# # 列表常用操作
# mylist = ["cast", "it", "python"]
# index = mylist.index("it")
# print(f"it在列表中的下标索引值是: {index}")
#
# mylist[0] = "boy"  # 修改对应下标的值
# print(mylist)
#
# mylist.insert(1, "best")
# print(f"插入元素后是：{mylist}")
#
# mylist.append("girl")
# print(f"尾部插入元素：{mylist}")
# # extend追加
# mylist2 = ["good", "very", "big"]
# mylist.extend(mylist2)
# print(f"追加插入一个列表：{mylist}")
#
# # del 方式删除
# mylist3 = ["good", "very", "big"]
# del mylist3[2]
# print(f"del 方式删除：{mylist3}")
#
# # pop 方式删除
# mylist4 = ["good", "very", "big"]
# element = mylist4.pop(2)
# print(f"pop 方式删除：{mylist4}, {element}")
#
# # remove 方式删除
# mylist5 = ["good", "very", "big", "good", "very", "big"]
# mylist5.remove("big")  # 只能删除最先的一个
# print(f"remove 方式删除:{mylist5}")
#
# # clear 方式删除，清空元素
# mylist6 = ["good", "very", "big", "good", "very", "big"]
# mylist6.clear()
# print(f"clear 方式删除，清空元素:{mylist6}")
#
# # count 统计元素
# mylist7 = ["good", "very", "big", "good", "very", "big"]
# count = mylist7.count("good")
# print(f"count 方式，统计元素:{count}")
#
# # len 统计全部元素
# mylist8 = ["good", "very", "big", "good", "very", "big"]
# count = len(mylist8)
# print(f"len 统计全部元素:{count}")

# # 常用功能练习
# age = [21, 25, 21, 23, 20, 22]
# age.append(31)
# age.extend([29, 33, 30])
# num1 = age.pop(0)
# print(f"{num1}")
# index = age.index(31)
# print(f"{index}, {age}")

# # 序列--切片
# my_list = [0, 1, 2, 3, 4, 5, 6]  # 对list进行切片
# result1 = my_list[1:4]
# result5 = my_list[3:1:-1]  # 从3开始， 到1结束， 步长为-1
# print(f"结果1：{result1}")
# print(f"结果5：{result5}")
#
# my_tuple = (0, 1, 2, 3, 4, 5, 6)  # 对tuple进行切片
# result2 = my_tuple[:]   # 起始不写等于由头到尾，步长为1可以省略
# result6 = my_tuple[::-2]  # 由头到尾，反向切片，步长为-2
# print(f"结果2：{result2}")
# print(f"结果6：{result6}")
#
# my_str = "0123456"  # 对str进行正向切片
# result3 = my_str[::2]
# result4 = my_str[::-1]
# print(f"结果3：{result3}")
# print(f"结果4：{result4}")
#
# # "万国薪月，员序程做，nohtyP学"
# my_str1 = "万国薪月，员序程做，nohtyP学"
# result7 = my_str1[7:4:-1]   # 方法1
# print(f"结果7：{result7}")
# result8 = my_str1.split("，")[1].replace("做", "")[::-1]
# print(f"结果8：{result8}")


# 集合set 不支持下标索引，与列表一样，允许修改的，不需要重复

# my_set = {"I", "have", "a", "little", "dog"}
# my_set.add("cat")  # 集合  add 添加元素
# print(f"添加元素后结果是：{my_set}")
# my_set.remove("dog")  # 集合  remove 移除元素
# print(f"移除元素后结果是：{my_set}")
# element = my_set.pop()  # 集合 pop 随机取出元素
# print(f"随机取出元素后结果是：{my_set}")
# my_set.clear()  # 集合 clear 清空元素
# print(f"随机取出元素后结果是：{my_set}")

# # 取差集 difference
# set1 = {1, 2, 3}
# set2 = {1, 5, 6 }
# set3 = set1.difference(set2)
# print(f"取差集后的结果:{set3}")
# print(f"取差集后，原有set1的内容：{set1}")
# print(f"取差集后，原有set2的内容：{set2}")
#
# set1.difference_update(set2)  # 在集合1里面删除和集合2相同的元素
# print(f"消除差集后，set1的内容：{set1}")   # 集合1被修改
# print(f"消除差集后，set2的内容：{set2}")   # 集合2不变
#
# set4 = set1.union(set2)  # 合并集合 ，不修改原集合，结果会被去重
# print(f"合并集合后，set3的内容：{set4}")
#
# num = len(set4)  # 不统计重复的元素
# print(f"统计元素容：{num}")
#
# for element in set4: # 集合不支持下标索引，无法使用while遍历，但可以使用for循环
#     print(f"集合的元素有：{element}")

# # dict 字典 不可使用下标索引，只能使用key
# my_dict1 = {"张三": 99, "李四": 88,"王五": 77}
# my_dict2 = {}
# my_dict3 = dict()
# score = my_dict1["张三"]   # dict 基本使用
# print(f"张三的考试分数：{score}")

# # dict的嵌套使用
# stu_score_dict = {
#     "张三": {
#         "语文": 77,
#         "数学": 66,
#         "英语": 33,
#     }, "李四": {
#         "语文": 88,
#         "数学": 99,
#         "英语": 55,
#     },  "王五": {
#         "语文": 78,
#         "数学": 58,
#         "英语": 98,
#     }
# }
# print(f"学生的考试信息：{stu_score_dict}")
# score = stu_score_dict["王五"]["语文"]
# print(f"张三的语文分数：{score}")


# my_dict = {"张三": 99, "李四": 88, "王五": 77}
# my_dict["叶六"] = 66  # 添加字典元素
# print(f"字典新增元素后：{my_dict}")
# my_dict["张三"] = 90  # 修改字典元素
# print(f"字典修改元素后：{my_dict}")
# score = my_dict.pop("张三")   # 删除字典元素
# print(f"移除张三：{my_dict}, 张三的分数：{score}")
# my_dict.clear()  # 清空字典元素
# print(f"字典被清空后的内容：{my_dict}")
# my_dict = {"张三": 99, "李四": 88, "王五": 77}
# keys = my_dict.keys()     # 获取字典中所有key
# print(f"获取全部key：{keys}")
# for key in keys:    # 遍历的方法1
#     print(f"字典的key是：{key}")
#     print(f"字典的value：{my_dict[key]}")
#
# for key in my_dict:   # 遍历的方法2
#     print(f"2字典的key是：{key}")
#     print(f"2字典的value：{my_dict[key]}")

# # 练习，员工升职加薪
# my_dict = {
#     "王力红": {"部门": "科技部",
#             "工资": 3000,
#             "级别": 1
#             },
#     "周杰轮": {"部门": "市场部",
#             "工资": 3000,
#             "级别": 2
#             },
#     "林俊姐": {"部门": "市场部",
#             "工资": 7000,
#             "级别": 3
#             },
#     "张学由": {"部门": "科技部",
#             "工资": 4000,
#             "级别": 1
#             },
#     "刘德花": {"部门": "科技部",
#             "工资": 6000,
#             "级别": 2
#             }
#
# }
# print(f"全体员工当前信息如下：{my_dict}")
# for key in my_dict:
#     if my_dict[key]["级别"] == 1:
#         my_dict[key]["级别"] = 2
#         my_dict[key]["工资"] += 1000
#
# print(f"全体员工级别为1的员工完成升职加薪后：{my_dict}")
