"""
i = 0
while i < 100:
    print("hello")
    i += 1

# 1到100的和
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(f"1-100的和：{sum}")


#猜数据，直到中了为止
import random
num = random.randint(1, 100)
count = 0
flag = True
while flag:
    guess_num = int(input("请输入数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("数字猜大了")

        else:
            print("数字猜小了")

print(f"共猜了{count}次")



# 控制行的循环   乘法表
i = 1
while i<= 9:
    # 控制每一行的循环
    j = 1
    while j<= i:
        print(f"{j} * {i} = {j * i }\t", end='')
        j += 1
    i += 1
    print()



# for 循环，轮询机制，一个个地去做，没有循环条件，循环取决于被处理的数据，无法构建无限循环
# 基础语法，简单例子如下
name = "it mans"
for x in name:
    print(x)

# 数一下有多少个o
name = "it supports room very good"
count = 0
for x in name:
    if x == "o":
         count += 1
print(f"共含：{count}个o字母")


# rang基本语句
for x in range(10):
    print(x)

for x in range(5, 10):
    print(x)

# 步长默认是1，现在修改为2，间隔2取值
for x in range(5, 10, 2):
    print(x)

# for循环简单例子
for x in range(10):
    print("送玫瑰花")

# 求1-100中的偶数数量
count = 0
for x in range(1, 100):
    if x % 2 == 0:
        count += 1
print(f"偶数数量为：{count}个")


# for 循环嵌套
i = 0
for i in range(1, 101):
    print(f"今天是本月第{i}次加油")

    for j in range(1, 24):
        print(f"{j}升油")
    print("停")
print(f"第{i}天，穷s了")

# # for循环制作99乘法表
#
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {j * i}\t", end='')
#     # 外层循环可以通过print输入一个回车符
#     print()

"""
# 发工资案例
# money = 10000
# for i in range(1, 21):
#     import random
#     num = random.randint(1, 10)
#     if num < 5:
#         print(f"员工{i}，绩效{num}，低于5，不发工资，下一位。")
#         continue
#     if money > 0:
#         money -= 1000
#         print(f"向员工{i}发放工资1000,账户余额还剩{money}")
#     else:
#         print(f"当前余额为{money},余额不足，不发工资了，下次再来")
#         break











