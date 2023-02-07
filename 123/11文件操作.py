# 文件编码  使用通用格式 UTF-8
# 打开文件
import time

f = open("F:/py/测试.txt", "r", encoding="UTF-8")
print(type(f))
# 读取文件
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部内容的结果：{f.read()}")  # 会从上次结尾处接着读取
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容：{lines}")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行：{line1}")
# print(f"第二行：{line2}")
# print(f"第三行：{line3}")

# # for循环读取文件行
# for line in f:
#     print(f"每一行数据：{line}")

# # 文件的关闭
#
# f.close()
# time.sleep(50000)   # 打开文件占用的时间
# with open 的使用方法
with open("F:/py/测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据：{line}")  # 此方法能自动关闭文件

time.sleep(500000)
