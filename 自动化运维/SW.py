from datetime import datetime
import multiprocessing
import os
import re
import time
from multiprocessing.pool import ThreadPool
from telnetlib import Telnet
import paramiko

pool = ThreadPool(10)


class Switch:
    def __init__(self, host, username, password, super_password, cmd):
        self.error_txt = ''
        self.connected = False
        self.tn = None
        self.ssh = None
        self.host = host
        self.username = username
        self.password = password
        self.super_password = super_password
        self.brand = None
        self.cmd = cmd
        self.login = False

    def test(self):
        print(self.username)
        print(self.host)

    # 设置交换机ssh方式登录交互机
    def ssh(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.connect(hostname=self.host, username=self.username, password=self.password, port=22)

    # 登录交换机的方法
    def huawei_telnet_login(self):
        # 设置交换机telnet方式登录交换
        try:
            self.tn = Telnet(self.host, port=23, timeout=3)
            self.connected = True
        except Exception as ee:
            # 否则表示Telnet失败
            self.connected = False
            self.error_txt = self.host + ',Telnet失败\n'
            with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                connect_fail.write('\n' + datetime.now().date().isoformat() + self.error_txt)
            print(self.error_txt)
            print(f"{self.host}连接失败，错误原因：{ee}")
        if self.connected:
            index, a, b = self.tn.expect([b'Username:', b'Password:'], timeout=1)
            if index == 0:
                try:
                    self.tn.write(self.username.encode('ascii') + b'\n')
                    self.tn.read_until(b'Password:', timeout=1)
                    self.tn.write(self.password.encode('ascii') + b'\n')
                    self.login = True
                    # output1 = self.tn.read_very_eager().decode()
                    # print(output1)
                    # if '>' in output1:
                    #     self.login = True
                    #     if self.login:
                    #         print(f'{self.host}账号登录成功')
                    #     if not self.login:
                    #         print(f'{self.host}账号登录失败')

                except:
                    self.login = False
                    print(f'{self.host}账号登录失败')

            elif index == 1:
                try:
                    self.tn.write(self.password.encode('ascii') + b'\n')
                    # output2 = self.tn.read_very_eager().decode()

                    # if '>' in output2:
                    #     self.login = True
                    #     if self.login:
                    #         print(f'{self.host}密码登录成功')
                    #     if not self.login:
                    #         print(f'{self.host}密码登录失败')

                except:
                    print(f'{self.host}密码登录失败')
            else:
                print(f'{self.host}登录失败')

            self.tn.read_until(b'>', timeout=1)
            self.tn.write(b"screen-length 0 temporary" + b"\n")
            self.tn.read_until(b'>', timeout=1)
            self.tn.write(b'sys' + b'\n')
            if self.login:
                index, f, g = self.tn.expect([b'>', b']'], timeout=1)
                if index == 0:
                    self.tn.write(b'su' + b'\n')
                    self.tn.read_until(b'Password:', timeout=1)
                    self.tn.write(self.super_password.encode() + b'\n')
                    self.tn.read_until(b'>', timeout=1)
                    self.tn.write(b"screen-length 0 temporary" + b"\n")
                    self.tn.read_until(b'>', timeout=1)
                    self.tn.write(b'sys' + b'\n')
                    print(f'{self.host}提权成功')
                elif index == 1:
                    print(f'{self.host}提权成功')
                else:
                    pass
                    print(f'{self.host}提权失败')
                self.tn.read_until(b"]", timeout=1)

        if not self.connected:
            print('跳过')
            pass
        return self.tn

    def c_telnet_login(self):
        pass

    # 判断交换机品牌
    def brand(self):
        pass

    # 判断远程连接方式是telnet还是SSH
    def connect(self):
        pass

    # 查看交换机sn码的方法
    def sn_switch(self):
        pass

    # 查看交换机光模块sn码的方法
    def sn_module(self):
        pass

    # 修改交换机全局配置的方法
    def global_conf(self):
        for cmds in self.cmd:
            if self.tn.read_until(b"]", timeout=1).decode('ascii'):
                self.tn.write(cmds.encode('ascii') + b'\n')
                time.sleep(1)
                self.tn.read_until(b"]", timeout=1).decode('ascii')
                output = self.tn.read_very_eager().decode()
                print(output)
                # print(self.cmd + '写入成功')
                time.sleep(0.5)
        return self.tn

    # 修改交换机端口配置的方法
    def interface_conf(self):
        pass

    def close(self):
        self.tn.close()
        print('全部配置刷入完成')
        # def run(host_, username_, password_, super_, cmd_list_):
        #     for cmd_ in cmd_list_:
        #         sw = Switch(host=host_, username=username_, password=password_, super_password=super_, cmds=cmd_)
        #         sw.huawei_telnet_login()
        #         sw.global_conf()
        #         sw.close()



if __name__ == '__main__':
    # path = os.getcwd()
    # if not os.path.exists(path + 'info.csv'):
    #     f = open(path + 'info.csv', 'w', newline='')

    cmd_list = list()
    host_list = list()
    login_info = list()
    try:
        with open('cmds.txt', 'r', encoding='UTF-8') as cmd_data:
            cmd = cmd_data.readlines()
            for c in cmd:
                c = c.strip()
                # print(c)
                cmd_list.append(c)

        with open('host_list.txt', 'r', encoding='UTF-8') as host_data:
            ip_list = host_data.readlines()
            for ip in ip_list:
                ip = ip.strip()
                # print(ip)
                host_list.append(ip)

        with open('login_info.txt', 'r', encoding='UTF-8') as login_data:
            login_info = login_data.read()
            username = re.findall('username:(.*)', login_info)[0]
            password = re.findall('password:(.*)', login_info)[0]
            super_password = re.findall('super:(.*)', login_info)[0]
    except Exception as e:
        print(f"读取出错：{e}")

    for host in host_list:
        sw = Switch(host=host, username=username, password=password, super_password=super_password, cmd=cmd_list)
        try:
            sw.huawei_telnet_login()
        except:
            pass
            sw.global_conf()
            sw.close()
        print(f'完成{host}')

    # for host in host_list:
    #     task = pool.apply_async(run, args=(host, username, password, super_password, cmd_list))
    #
    # pool.close()
    # pool.join()

    # run_process = multiprocessing.Process(
    #     target=run(host_list_=host_list, username_=username, password_=password, super_=super_password,
    #                cmd_list_=cmd_list))
    # run_process.start()
