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


# 导入所需的库
import pysnmp
import xlwt
import os

# 连接到华三交换机
snmp_client = pysnmp.client.SnmpClient(host='192.168.56.10', port=161, community='public')
# 创建xls文件
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Sheet1')
# 查询每个端口下的光模块sn
for port in range(1, 10):
    oid = '1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11.{}'.format(port)
    sn = snmp_client.get(oid)
    sheet.write(port, 0, port)
    sheet.write(port, 1, sn)
# 保存xls文件
workbook.save(os.path.join(os.getcwd(), 'sn.xls'))
