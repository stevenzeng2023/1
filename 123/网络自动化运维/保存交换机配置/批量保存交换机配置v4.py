import telnetlib
import textwrap
import time
from telnetlib import Telnet
import re
from multiprocessing import Process

# 创建交换机类
class Switch:
    def __init__(self, host, username1, username2, password1, password2, super_password1, super_password2, brand):
        self.host = host
        self.username1 = username1
        self.username2 = username2
        self.password1 = password1
        self.password2 = password2
        self.super_password1 = super_password1
        self.super_password2 = super_password2
        self.brand = brand

    # 设置交换机的登录方法
    def login(self):
        try:
            with telnetlib.Telnet(self.host, port=23, timeout=3) as tn:
                # 设置判断交换机品牌的条件
                index, a, b = tn.expect([b'Login:', b'Username:'], timeout=1)
                # 关键字为Login：的是H3C
                if index == [0]:
                    self.brand = 'H3C'
                    tn.write(self.username1 + b'\n')
                    tn.read_until(b'Password:', timeout=1)
                    tn.write(password + b'\n')
                    index1, a1, b1 = tn.expect([b'>', b'Username'])
                    tn.read_until(b'>', timeout=1)
                    tn.write(b'su' + b'\n')
                    tn.read_until(b'Password:', timeout=1)
                    tn.write(super_password + b'\n')
                    tn.read_until(b'>', timeout=1)
                    tn.write(b'sys' + b'\n')

                # 关键字为Username：的是华为或者思科
                elif index == [1]:
                    self.brand = 'HUAWEI_CISCO'
                    tn.write(self.username)

        except:




    # 设置区分交换机品牌的方法
    def brand(self):
        pass

    # 设置发送命令方法
    def cmds(self):
        pass

# 获取数据的方法
def get_data(self):
        pass
# 执行交换机类的方法
def execute():
    pass

# 设置多进程运行方法
def process_pool():
    pass


if __name__ == '__main__':
    host_list = list()
    login_list = list()

    try:
        with open('host_list.txt', 'r', encoding='UTF-8') as host_data:
            hosts = host_data.readlines()
            for host in hosts:
                host = host.strip()
                host_list.append(host)
        # print(host_list)
    except:
        print('读取出错')
    try:
        with open('login_info.txt', 'r', encoding='UTF-8') as login_data:
            login = login_data.read()
            username = re.findall('username=(.*)', login)[0]
            password = re.findall('password:(.*)', login)[0]
            super_password = re.findall('super_password:', login)[0]
    except:
        print('读取出错')

    for host in host_list:
        s = Switch(host, username, password, super_password)

