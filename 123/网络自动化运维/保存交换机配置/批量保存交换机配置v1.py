import time
import re
from datetime import datetime
from telnetlib import Telnet
from multiprocessing.pool import ThreadPool
import os

pool = ThreadPool(10)


# 华为交换机的命令执行方法
def huawei_model(host, username, password, su, cmds):
    try:
        with Telnet(host, port=23, timeout=3) as telnet:
            index, obj, output = telnet.expect([b'Username:', b'Password:'], timeout=1)
            if index == 0:
                telnet.write(username.encode('ascii') + b'\n')
                telnet.read_until(b'Password:', timeout=1)
                telnet.write(password.encode('ascii') + b'\n')
            elif index == 1:
                telnet.write(password.encode('ascii') + b'\n')
            else:
                print('unknown prompt!')
            telnet.read_until(b'>', timeout=1)
            telnet.write(b'sys' + b'\n')
            index, obj, output = telnet.expect([b'>', b']'], timeout=1)
            if index == 0:
                telnet.write(b'su' + b'\n')
                telnet.read_until(b'Password:', timeout=1)
                telnet.write(su.encode() + b'\n')
                telnet.read_until(b'>', timeout=1)
                telnet.write(b"screen-length 0 temporary" + b"\n")
                telnet.read_until(b'>', timeout=1)
                telnet.write(b'sys' + b'\n')
            elif index == 1:
                pass
            else:
                print('unknown prompt!')

            telnet.read_until(b">", timeout=1)

            for cmd in cmds:
                telnet.write(cmd.encode('ascii') + b'\n')
                time.sleep(2)
                output = telnet.read_very_eager().decode()
                txt(host + '-' + datetime.now().date().isoformat(), output)

    except Exception as e:
        print(f"连接错误{e}")


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
    host_list = list()
    login_info = list()
    show_cmds = ['dis cur']
    # username = 'admin'
    # password = '123'
    # su = '123'
    try:
        with open('保存交换机配置/host_list.txt', 'r', encoding='UTF-8') as host_data:
            ip_list = host_data.readlines()
            for ip in ip_list:
                ip = ip.strip()
                host_list.append(ip)
        with open('保存交换机配置/login_info.txt', 'r', encoding='UTF-8') as login_data:
            login_info = login_data.read()
            username = re.findall('username:(.*)', login_info)[0]
            password = re.findall('password:(.*)', login_info)[0]
            su = re.findall('super:(.*)', login_info)[0]
    except:
        print('读取出错')
    for host in host_list:
        task = pool.apply_async(huawei_model, args=(host, username, password, su, show_cmds))

    pool.close()
    pool.join()
