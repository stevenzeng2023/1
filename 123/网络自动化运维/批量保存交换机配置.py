import telnetlib
import re
from multiprocessing.pool import ThreadPool

pool = ThreadPool(10)

class Huawei_switch:
    def __init__(self):
        self.host = None
        self.password = None
        self.username = None
        self.super = None
        self.telnet = None
        self.connected = False

    def login(self):
        """
        登录交换机的方法以及反馈登录结果
        :return:
        """

        try:
            self.telnet = telnetlib.Telnet(self.host, port=23, timeout=3)
            self.connected = True
            print(f"{self.host}登录成功")
        except:
            print(f"{self.host}登录失败")

            if self.connected:
                get_login_word = self.telnet.read_until(b":", timeout=3)

    def switch_model(self):
        """
        识别交换机的型号
        :return:
        """
        pass

    # 华为交换机的命令执行方法
    def huawei_model(self):
        if self.connected:
            self.telnet.read_until(b"login:", timeout=1)
            self.telnet.write(self.username + b"\n")
            self.telnet.read_until(b"Password:", timeout=1)
            self.telnet.write(self.password + b"\n")
            self.telnet.read_until(b">", timeout=1)
            self.telnet.write(b"screen-length 0 temporary" + b"\n")
            self.telnet.read_until(b">", timeout=1)
            self.telnet.write(b"dis cur" + b"\n")


if __name__ == "__main__":
    # 读取主机信息
    host_list = list()
    try:
        with open('保存交换机配置/host_list.txt', 'r', encoding='UTF-8') as host_data:
            ip_list = host_data.readlines()
            for ip in ip_list:
                ip = ip.strip()
                host_list.append(ip)
    except:
        print('读取出错')

    # 读取登录信息
    # login_txt = ''
    # with open('login_info.txt', 'r') as login_data:
    #     login_txt = login_data.read()
    #     username = re.findall('username=(.*)', login_txt)[0].strip()
    # print(login_txt)
