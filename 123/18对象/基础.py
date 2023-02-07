# # 设计一个类
# class Student:
#     name = None
#     gender = None
#     nationality = None
#     native_place = None
#     age = None
#
# # 创建一个对象
# stu_1 = Student()
#
# # 对象属性赋值
# stu_1.name = "张三"
# stu_1.gender = "男"
# stu_1.nationality = "中国"
# stu_1.native_place = "广东"
# stu_1.age = 30
#
# # 获取对象中记录的信息
# print(stu_1.name)
# print(stu_1.gender)
# print(stu_1.nationality)
# print(stu_1.age)

# # 面向对象的编程思想
# # 设计一个闹钟类
# class Clock:
#     id = None
#     price = None
#
#     def ring(self):
#         import winsound
#         winsound.Beep(2000, 3000)
#
# # 构建2个闹钟对象并让其工作
# clock1 = Clock()
# clock1.id = "003032"
# clock1.price = 19.99
# print(f"闹钟ID：{clock1.id},价格：{clock1.price}")
# clock1.ring()
#
# clock2 = Clock()
# clock2.id = "003033"
# clock2.price = 21.99
# print(f"闹钟ID：{clock2.id},价格：{clock2.price}")
# clock2.ring()

# 构造方法__init__
class Student:
    name = Non  # 可以不写
    age = None  # 可以不写
    tel = None  # 可以不写

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建一个类对象")

stu = Student("张三", 31, "1234568910")
print(stu.name)
print(stu.age)
print(stu.tel)



