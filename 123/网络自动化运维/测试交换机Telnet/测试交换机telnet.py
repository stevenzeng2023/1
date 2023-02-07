from telnetlib import Telnet
from concurrent.futures import ProcessPoolExecutor
from multiprocessing.pool import ThreadPool
import os
import re


def telnet_login(self):
    try:
        with Telnet(host=self.host, port=23, timeout=1) as tn:
            tn.read_until(b'username:', timeout=1)
            tn.write(b"Password:" + b'\n')
            tn.read_until(b'>', timeout=1)
            tn.write(b'su' + b'\n')
            tn.write(b"Password:" + b'\n')
            tn.write(b'libin110066' + b'\n')
            tn.read_until(b'>', timeout=1)
            tn.write(b'sys' + b'\n')
            if tn.read_until(b']', timeout=1):
                a = host + 'telnet成功'
                print(f"{a}")
    except:
        b = host + 'telnet失败'
        print(f"{b}")


def txt(name, text):
    # os.getcwd() 获取当前的工作路径；
    new = os.getcwd() + '\\cache\\'
    # 判断当前路径是否存在，没有则创建new文件夹
    if not os.path.exists(new):
        os.makedirs(new)

    # 在当前py文件所在路径下的new文件中创建txt
    x = new + name + '.txt'
    # 打开文件，open()函数用于打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
    file = open(x, 'w')

    # 写入内容信息
    file.write(text)

    file.close()
    print('文件创建成功', x)


if __name__ == "__main__":
    # 读取主机信息
    pool = ThreadPool(10)
    host_list = list()
    login_info = list()

    try:
        with open('host_list.txt', 'r', encoding='UTF-8') as host_data:
            ip_list = host_data.readlines()
            for ip in ip_list:
                ip = ip.strip()
                host_list.append(ip)
        with open('login_info.txt', 'r', encoding='UTF-8') as login_data:
            login_info = login_data.read()
            username = re.findall('username=(.*)', login_info)[0]
            password = re.findall('password=(.*)', login_info)[0]
            super_password = re.findall('super_password=(.*)', login_info)[0]
    except:
        print('读取出错')

    for host in host_list:
        task = pool.apply_async(telnet_login, args=(host, username, password, super_password))

    pool.close()
    pool.join()
