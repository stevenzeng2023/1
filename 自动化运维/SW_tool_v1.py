from datetime import datetime
import multiprocessing
import os
import re
import time
from multiprocessing.pool import ThreadPool
from telnetlib import Telnet
import paramiko
from threading import Lock

pool = ThreadPool(10)
mutex = Lock()


class Switch:
    def __init__(self, host, username, password, super_password):
        self.error_txt = list()
        self.connected = False
        self.tn = None
        self.ssh = None
        self.host = host
        self.username = username
        self.password = password
        self.super_password = super_password
        self.brand = None
        self.login = False
        self.power = False

    def test(self):
        print(self.username)
        print(self.host)

    # 设置交换机ssh方式登录交互机
    def ssh(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.connect(hostname=self.host, username=self.username, password=self.password, port=22)

    # 登录交换机的方法
    def telnet(self):
        # 设置交换机telnet方式登录交换
        try:
            self.tn = Telnet(self.host, port=23, timeout=3)
            self.connected = True
        except Exception as ee:
            # 否则表示Telnet失败
            self.connected = False
            self.error_txt = self.host + ',Telnet失败\n'
            # print(self.error_txt)
            mutex.acquire()
            with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + self.error_txt)
            print(f"{self.host}连接失败，错误原因：{ee}")
            mutex.release()
            time.sleep(1)
        return self.tn, self.error_txt

        # result = self.tn.read_very_eager().decode('ascii')
        # print(result)

    def huawei_login(self):
        if self.connected:
            index, a, b = self.tn.expect([b'Username:', b'Password:'], timeout=1)
            if index == 0:
                try:
                    self.tn.write(self.username.encode('ascii') + b'\n')
                    self.tn.read_until(b'Password:', timeout=1)
                    self.tn.write(self.password.encode('ascii') + b'\n')
                    get_login_word = self.tn.read_until(b">", timeout=3)
                    get_login_word = get_login_word.decode()
                    if '>' in get_login_word:
                        self.login = True
                        print(f'{self.host},以账号密码登录成功')
                    else:
                        print(f'{self.host},以账号密码登录失败')
                        mutex.acquire()
                        with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                            connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                        mutex.release()
                        time.sleep(1)
                        self.login = False



                except:
                    self.login = False
                    mutex.acquire()
                    with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                        connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                    mutex.release()
                    time.sleep(1)
                    print(f'{self.host},以账号密码登录失败')

            elif index == 1:
                try:
                    self.tn.write(self.password.encode('ascii') + b'\n')
                    get_login_word = self.tn.read_until(b">", timeout=3)
                    get_login_word = get_login_word.decode()

                    if '>' in get_login_word:
                        print(f'{self.host},以密码登录成功')
                        self.login = True
                        # return self.login
                    else:
                        print(f'{self.host},以密码登录失败')
                        mutex.acquire()
                        # self.error_txt.append(datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                        with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                            connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                        mutex.release()
                        time.sleep(1)
                        self.login = False
                        # return self.login, self.error_txt

                except:
                    print(f'{self.host},密码登录失败')
                    mutex.acquire()
                    with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                        connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                    mutex.release()
                    time.sleep(1)
                    self.login = False
            else:
                self.login = False
                print(f'{self.host},登录失败')
                mutex.acquire()
                with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                    connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                mutex.release()
                time.sleep(1)
            if self.login:
                self.tn.read_until(b'>', timeout=1)
                self.tn.write(b"screen-length 0 temporary" + b"\n")
                self.tn.read_until(b'>', timeout=1)
                self.tn.write(b'sys' + b'\n')
                index, f, g = self.tn.expect([b'>', b']'], timeout=1)
                if index == 0:
                    self.tn.write(b'su' + b'\n')
                    self.tn.read_until(b'Password:', timeout=1)
                    self.tn.write(self.super_password.encode() + b'\n')
                    self.tn.read_until(b'>', timeout=1)
                    self.tn.write(b"screen-length 0 temporary" + b"\n")
                    self.tn.read_until(b'>', timeout=1)
                    self.tn.write(b'sys' + b'\n')
                    get_power_word = self.tn.read_until(b']', timeout=1)
                    get_power_word = get_power_word.decode()
                    if ']' in get_power_word:
                        self.power = True
                        print(f'{self.host},提权成功')
                    else:
                        self.power = False
                        print(f'{self.host},提权失败')
                        mutex.acquire()
                        with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                            connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},提权失败')
                        mutex.release()
                        time.sleep(1)
                elif index == 1:
                    self.power = True
                    print(f'{self.host},提权成功')
                else:
                    self.power = False
                    print(f'{self.host},提权失败')
                    mutex.acquire()
                    with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                        connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},提权失败')
                    mutex.release()
                    time.sleep(1)

                # return self.tn, self.login

        if not self.connected:
            print(self.host + '，无法进行操作')
            pass
            # return self.tn, self.login

        return self.tn, self.power, self.power, self.error_txt

    def H3C_login(self):
        if self.connected:
            index, a, b = self.tn.expect([b'Login:', b'Password:'], timeout=1)
            if index == 0:
                try:
                    self.tn.write(self.username.encode('ascii') + b'\n')
                    self.tn.read_until(b'Password:', timeout=1)
                    self.tn.write(self.password.encode('ascii') + b'\n')
                    get_login_word = self.tn.read_until(b">", timeout=3)
                    get_login_word = get_login_word.decode()
                    if '>' in get_login_word:
                        self.login = True
                        print(f'{self.host},以账号密码登录成功')
                    else:
                        print(f'{self.host},以账号密码登录失败')
                        mutex.acquire()
                        with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                            connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                        mutex.release()
                        time.sleep(1)
                        self.login = False



                except:
                    self.login = False
                    mutex.acquire()
                    with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                        connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                    mutex.release()
                    time.sleep(1)
                    print(f'{self.host},以账号密码登录失败')

            elif index == 1:
                try:
                    self.tn.write(self.password.encode('ascii') + b'\n')
                    get_login_word = self.tn.read_until(b">", timeout=3)
                    get_login_word = get_login_word.decode()

                    if '>' in get_login_word:
                        print(f'{self.host},以密码登录成功')
                        self.login = True
                        # return self.login
                    else:
                        print(f'{self.host},以密码登录失败')
                        mutex.acquire()
                        # self.error_txt.append(datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                        with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                            connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                        mutex.release()
                        time.sleep(1)
                        self.login = False
                        # return self.login, self.error_txt

                except:
                    print(f'{self.host},密码登录失败')
                    mutex.acquire()
                    with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                        connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                    mutex.release()
                    time.sleep(1)
                    self.login = False
            else:
                self.login = False
                print(f'{self.host},登录失败')
                mutex.acquire()
                with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                    connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},登录失败')
                mutex.release()
                time.sleep(1)
            if self.login:
                self.tn.read_until(b'>', timeout=1)
                self.tn.write(b"screen-length 0 temporary" + b"\n")
                self.tn.read_until(b'>', timeout=1)
                self.tn.write(b'sys' + b'\n')
                index, f, g = self.tn.expect([b'>', b']'], timeout=1)
                if index == 0:
                    self.tn.write(b'su' + b'\n')
                    self.tn.read_until(b'Password:', timeout=1)
                    self.tn.write(self.super_password.encode() + b'\n')
                    self.tn.read_until(b'>', timeout=1)
                    self.tn.write(b"screen-length 0 temporary" + b"\n")
                    self.tn.read_until(b'>', timeout=1)
                    self.tn.write(b'sys' + b'\n')
                    get_power_word = self.tn.read_until(b']', timeout=1)
                    get_power_word = get_power_word.decode()
                    if ']' in get_power_word:
                        self.power = True
                        print(f'{self.host},提权成功')
                    else:
                        self.power = False
                        print(f'{self.host},提权失败')
                        mutex.acquire()
                        with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                            connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},提权失败')
                        mutex.release()
                        time.sleep(1)
                elif index == 1:
                    self.power = True
                    print(f'{self.host},提权成功')
                else:
                    self.power = False
                    print(f'{self.host},提权失败')
                    mutex.acquire()
                    with open('connect_fail.txt', 'a', encoding='UTF-8') as connect_fail:
                        connect_fail.write('\n' + datetime.now().date().isoformat() + ' ' + f'{self.host},提权失败')
                    mutex.release()
                    time.sleep(1)

                # return self.tn, self.login

        if not self.connected:
            print(self.host + '，无法进行操作')
            pass
            # return self.tn, self.login

        return self.tn, self.power, self.power, self.error_txt


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
    def global_conf(self, cmds):
        if self.login:
            try:
                self.tn.write(cmds.encode('ascii') + b'\n')
                print(f'为{self.host},写入命令 ' + cmds + '，写入成功')
                time.sleep(0.5)
            except Exception as g:
                print(f'为{self.host},写入 ' + cmds + f'失败，失败原因：{g}')

        return self.tn

    # 修改交换机端口配置的方法
    def interface_conf(self):
        pass

    def close(self):
        self.tn.close()

        # print('全部配置刷入完成')
        # def run(host_, username_, password_, super_, cmd_list_):
        #     for cmd_ in cmd_list_:
        #         sw = Switch(host=host_, username=username_, password=password_, super_password=super_, cmds=cmd_)
        #         sw.huawei_telnet_login()
        #         sw.global_conf()
        #         sw.close()


def run(host, username, password, super_password, cmd_list, brand):
    sw = Switch(host=host, username=username, password=password, super_password=super_password)
    try:
        time.sleep(0.5)
        sw.telnet()
        time.sleep(0.5)
        if 'huawei' in brand:
            power = sw.huawei_login()[2]
            time.sleep(0.5)
            if power:
                for cmds in cmd_list:
                    sw.global_conf(cmds=cmds)
                    time.sleep(0.5)
            sw.close()
            print(f'{host}，已处理')
        elif 'H3C' in brand:
            power = sw.H3C_login()[2]
            time.sleep(0.5)
            if power:
                for cmds in cmd_list:
                    sw.global_conf(cmds=cmds)
                    time.sleep(0.5)
            sw.close()
            print(f'{host}，已处理')


    except Exception as eee:
        print(f'{host},处理失败,失败原因:{eee}')


if __name__ == '__main__':
    # path = os.getcwd()
    # if not os.path.exists(path + 'info.csv'):
    #     f = open(path + 'info.csv', 'w', newline='')

    cmd_list = []
    host_list = list()
    login_info = list()
    try:
        with open('cmds.txt', 'r', encoding='UTF-8') as cmd_data:
            cmd = cmd_data.readlines()
            for c in cmd:
                c = c.strip()
                cmd_list.append(c)
                # print(cmd_list)

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
            brand = re.findall('brand:(.*)', login_info)[0]
    except Exception as e:
        print(f"读取出错：{e}")

    # for host in host_list:
    #     sw = Switch(host=host, username=username, password=password, super_password=super_password)
    #     try:
    #         sw.huawei_telnet()
    #         info = sw.huawei_login()
    #         # time.sleep(2)
    #         # get_w = sw.huawei_telnet().read_very_eager()
    #         # get_w = get_w.decode()
    #         # print(get_w)
    #         if info:
    #             for cmd in cmd_list:
    #                 sw.global_conf(cmds=cmd)
    #         sw.close()
    #     except Exception as eee:
    #         print(f'程序出错:{eee}')
    #     print(f'{host}已处理')

    for host in host_list:
        task = pool.apply_async(run, args=(host, username, password, super_password, cmd_list, brand))

    pool.close()
    pool.join()

    # run_process = multiprocessing.Process(
    #     target=run(host_list_=host_list, username_=username, password_=password, super_=super_password,
    #                cmd_list_=cmd_list))
    # run_process.start()
