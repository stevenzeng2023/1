#  多并发
#  index判断
#
#
# from telnetlib import Telnet
#
#
# def login(host):
#     tn = Telnet(host, port=23, timeout=5)
#     tn.read_until(b'assword:', timeout=1)
#     tn.write(b'123' + b'\n')
#     tn.read_until(b'>', timeout=1)
#     tn.write(b'screen-length 0 temporary' + b'\n')
#     tn.read_until(b'>', timeout=1)
#     tn.write(b'display current-configuration' + b'\n')
#     output = tn.read_very_eager().decode()
#     print(output)
#
#
# if __name__ == '__main__':
#     login('192.168.56.10')
# import time
# from telnetlib import Telnet
# host = '192.168.56.10'
# with Telnet(host, port=23, timeout=1) as tn:
#     if
#     tn.read_until(b':', timeout=1)
#     # tn.write(b'admin' + b'\n')
#     tn.read_until(b'Password:', timeout=1)
#     tn.write(b'123' + b'\n')
#     tn.read_until(b'>', timeout=1)
#     tn.write(b'screen-length 0 temporary' + b'\n')
#     tn.read_until(b'>', timeout=1)
#     tn.write(b'dis cur' + b'\n')
#     time.sleep(2)
#     output = tn.read_very_eager().decode()
#     print(output)
# global host11
# with open('host_list.txt', 'r', encoding='UTF-8') as host_data:
#
#     for i in host_data:
#         host = i.split()
#
#         print(host)
# import re
# hosts_list = list()
# try:
#     with open('host_list.txt', 'r', encoding='UTF-8') as host_data:
#         host_list = host_data.readlines()
#         for host in host_list:
#             host = host.strip()
#             hosts_list.append(host)
#         print(hosts_list)
#     with open('login_info.txt', 'r', encoding='UTF-8') as login_data:
#         login_info = login_data.read()
#         username = re.findall('username:(.*)', login_info)
#         password = re.findall('password:(.*)', login_info)
#         su = re.findall('super:(.*)', login_info)
#         print(username, password, su)
# except:
#     print('读取出错')
# import datetime
# for i in host_data:
#     print(i)

# 读取登录信息
# login_txt = ''
# with open('login_info.txt', 'r') as login_data:
#     login_txt = login_data.read()
#     username = re.findall('username=(.*)', login_txt)[0].strip()
# print(login_txt)

# from telnetlib import Telnet
#
# tn = Telnet(host='192.168.56.20', port=23, timeout=2)
# tn.read_until(b'Password', timeout=1)
# tn.write(b'huawei' + b'\n')
#
# get_login_word = tn.read_until(b":", timeout=3)
# get_login_word = get_login_word.decode()
# print(get_login_word)
# import os
# import csv


# def txt(name, text):
#     # os.getcwd() 获取当前的工作路径；
#     new = os.getcwd() + '\\cache\\'
#     # 判断当前路径是否存在，没有则创建new文件夹
#     if not os.path.exists(new):
#         os.makedirs(new)
#
#     # 在当前py文件所在路径下的new文件中创建txt
#     x = new + name + '.csv'
#
#     # 打开文件，open()函数用于打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
#     file = open(x, 'w')
#
#     # 写入内容信息
#     csv_file = csv.writer(file)
#     csv_file.writerow(text)
#
#     file.close()
#     print('文件创建成功', x)
#
#
# test = (['交换机IP', '交换机名称', '品牌', '端口号', '模块速率',
#          '模块接口类型', '模块SN'])
# txt('123', test)

from Switch import 