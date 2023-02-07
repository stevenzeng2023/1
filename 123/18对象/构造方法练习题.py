# 有一批学生需要录入系统，用类记录学生的信息

class student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


for num in range(1, 2):
    print(f"当前录入第{num}位学生信息，总共需录入5位学生信息。 ")
    name_info = str(input("请输入学生姓名："))
    age_info = str(input("请输入学生年龄："))
    address_info = str(input("请输入学生地址："))



student_info = student(name_info, age_info, address_info)
print(student_info)
