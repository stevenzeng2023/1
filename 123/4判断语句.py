"""
# 判断-布尔类型
bool_1 = True
bool_2 = False
result = 10 > 5
print(f"bool_1变量的内容是：{bool_1}, 类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}, 类型是：{type(bool_2)}")

num1 = 10
num2 = 10
print(f"10==10的结果：{num1 == num2}")

# if 语句
age = input(type(int))
if age >=18:
    print("已经成年了")
    print("该上大学了")


# 检查手机号码
num1 = 13726235584
num3 = 16675682908
num2 = int(input("请输入您老婆的手机号码："))

if num2 == num1:
    print("恭喜您，号码正确，请找老婆打款。")
elif num2 == num3:
    print("恭喜你，这个也对，请找您老婆打款。")
else:
    print("号码错误，请交罚款10元。")
print("祝你生活愉快！")

# 多重判断
num1 = int(input("请输入第一位嘉宾的号码："))
num2 = int(input("请输入第二位嘉宾的号码："))
if num2 == num1:
    print("恭喜你们，一次匹配成功！")
elif int(input("再试一次：")) == num1:
    print("恭喜你们，第二次匹配终于成功！")
else:
    print("匹配识别，再接再厉！")
"""
# 嵌套判断
# print("欢迎来到我家动物园！")
# if int(input("请输入您的年龄：")) >= 10:
#     print("您的年龄不符合免费游玩。")
#     print("如果是高级VIP，也能免费游玩。")
#     if int(input("请输入您的vip登记：")) > 3:
#         print("尊敬的高级会员，您可以免费游玩！")
#     else:
#         print("您需要补票10元。")
# else:
#     print("小朋友，欢迎光临！")

# age = int(input("请输入您的年龄："))
# if age >= 20:
#     print("您的年龄符合条件。")
#     year = int(input("请输入您的工龄："))
#     if year >= 2:
#         print("恭喜你符合所有条件，可以领取礼物。")
#     else:
#         print("抱歉，您工龄不符合条件，无法领取礼物。")
# else:
#     print("抱歉，实习生不符合条件领取礼物。")


# 判断语句猜数字
# 1.构建一个随机数字变量
import random
num = random.randint(1, 10)
guess_num = int(input("请输入你要猜的数字："))
# 使用if判断语句进行猜测
if guess_num == num:
    print("恭喜猜中了！")
else:
    if guess_num > num:
        print("你猜测的数字大了！")
    if guess_num < num:
        print("你猜测的数字小了！")
    guess_num = int(input("第二次输入你要猜的数字："))
    if guess_num == num:
        print("恭喜你第二次猜中了！")
    else:
        if guess_num > num:
            print("你猜测的数字大了！")
        if guess_num < num:
            print("你猜测的数字小了！")
        guess_num = int(input("第三次输入你要猜的数字："))
        if guess_num == num:
            print("恭喜你第三次猜中了！")
        else:
            print("三次机会用完，没猜中！")