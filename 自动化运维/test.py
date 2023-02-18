# import re
# import time
# from multiprocessing.pool import ThreadPool
# from telnetlib import Telnet
#
# import SW
# #
# # pool = ThreadPool(10)
# #
# #
# # def run(host_list_, username_, password_, super_, cmd_list_):
# #     for host_ in host_list_:
# #         for cmd_ in cmd_list_:
# #             sw = SW.Switch(host=host_, username=username_, password=password_, super_password=super_, cmds=cmd_)
# #             sw.huawei_telnet_login()
# #             sw.global_conf()
# #             sw.close()
# #             print('刷入全局配置完成')
# #
# #
# # cmd_list = list()
# # host_list = list()
# # login_info = list()
# # try:
# #     with open('cmds.txt', 'r', encoding='UTF-8') as cmd_data:
# #         cmd = cmd_data.readlines()
# #         for c in cmd:
# #             c = c.strip()
# #             cmd_list.append(c)
# #     with open('host_list.txt', 'r', encoding='UTF-8') as host_data:
# #         ip_list = host_data.readlines()
# #         for ip in ip_list:
# #             ip = ip.strip()
# #             host_list.append(ip)
# #     with open('login_info.txt', 'r', encoding='UTF-8') as login_data:
# #         login_info = login_data.read()
# #         username = re.findall('username:(.*)', login_info)[0]
# #         password = re.findall('password:(.*)', login_info)[0]
# #         super_password = re.findall('super:(.*)', login_info)[0]
# # except Exception as e:
# #     print(f"读取出错：{e}")
# # for host in host_list:
# #     task = pool.apply_async(run, args=(host_list, username, password, super_password, cmd_list))
# # pool.close()
# # pool.join()
#
# # cmd_list = list()
# host_list = list()
# login_info = list()
# try:
#     # with open('cmds.txt', 'r', encoding='UTF-8') as cmd_data:
#     #     cmd = cmd_data.readlines()
#     #     for c in cmd:
#     #         c = c.strip()
#     #         cmd_list.append(c)
#     with open('host_list.txt', 'r', encoding='UTF-8') as host_data:
#         ip_list = host_data.readlines()
#         for ip in ip_list:
#             ip = ip.strip()
#             host_list.append(ip)
#     with open('login_info.txt', 'r', encoding='UTF-8') as login_data:
#         login_info = login_data.read()
#         username = re.findall('username:(.*)', login_info)[0]
#         password = re.findall('password:(.*)', login_info)[0]
#         super_password = re.findall('super:(.*)', login_info)[0]
# except Exception as e:
#     print(f"读取出错：{e}")
#
# for host in host_list:
#     with Telnet(host, port=23, timeout=3) as tn:
#         index, obj, output = tn.expect([b'Username:', b'Password:'], timeout=1)
#         if index == 0:
#             tn.write(username.encode('ascii') + b'\n')
#             tn.read_until(b'Password:', timeout=1)
#             tn.write(password.encode('ascii') + b'\n')
#         elif index == 1:
#             tn.write(password.encode('ascii') + b'\n')
#         else:
#             print('unknown prompt!')
#         tn.read_until(b'>', timeout=1)
#         tn.write(b"screen-length 0 temporary" + b"\n")
#         tn.read_until(b'>', timeout=1)
#         tn.write(b'sys' + b'\n')
#         tn.read_until(b'>', timeout=1)
#         tn.write(b'dis cur' + b'\n')
#         time.sleep(2)
#         output = tn.read_very_eager().decode()
#         print(output)
#
# class A:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def he(self):
#         d = self.a + self.b
#         print(d)
#
# if __name__ == '__main__':
#     aa = 1
#     bb = 2
#     cc = 3
#     hh = A(aa, bb, cc)
#     hh.he()

import telnetlib  # 导入Telnetlib模块

host = "192.168.56.10"
user = "greeadmin"  # 定义四个变量，分别是地址、用户名、密码、和退出字符串
password = "cisco2900"
enter = "su"
exit_telnet = "quit"

tn = telnetlib.Telnet(host, 32771)  # 赋值tn，尝试以Telnet登录到192.168.142.128,32771。

tn.write(b"rn")  # 输入换行符，等于输入enter键。进入用户模式
tn.write(b"sun")  # 进入R3的特权模式
tn.read_until(b"Password: ")  # 用read_until检测关键字：Password
tn.write(password.encode('ascii') + b"n")  # 当符合关键字条件之后，输入用户名，并用n换行
tn.write(b"telnet 192.168.56.20n")  # 利用python将Telnet到R4的命令发送给R3

tn.read_until(b"Username: ")  # 登录到R4后，会提示Username，跟前面一样，读取关键字
tn.write(user.encode('ascii') + b"n")
tn.read_until(b"Password: ")  # 登录到R4后，读取关键字，并输入密码
tn.write(password.encode('ascii') + b"n")
# ----------------------------------------下面的配置都是网工烂熟于心的配置了，这里就不再介绍---------
tn.write(b"sun")
tn.write(b"123n")
tn.write(b"conf tn")
tn.write(b"int lo1n")
tn.write(b"ip add 2.2.2.2 255.255.255.0n")
tn.write(b"do sh ip int brn")
tn.write(b"endn")
tn.write(b"exitn")
tn.read_until(b"[Connection to")  # 检测是否退出了R4的Telnet，这里只需检测是否为[Connection开头即可。
tn.write(exit_telnet.encode('ascii') + b"n")  # 当检测到已经退出R4的Telnet，说明已经退回到R3的特权模式。这里再次输入exit退出。

tn.close()
print(tn.read_all().decode('ascii'))
