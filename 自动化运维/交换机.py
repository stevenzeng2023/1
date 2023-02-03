import os
import telnetlib

import paramiko


class Switch:
    def __int__(self, host, username, password, brand, super_password, command):
        self.host = host
        self.username = username
        self.password = password
        self.super_password = super_password
        self.brand = brand
        self.command = command


    # 登录交换机的方法
    def login(self):
        # 设置交换机telnet方式登录交换
        tn = telnetlib.Telnet(host=self.host, port=23, timeout=3)
        pass
        # 设置交换机ssh方式登录交互机
        ssh = paramiko.SSHClient()
        ssh.connect(hostname=self.host, username=self.username, password=self.password, port=22)
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
        pass

    # 修改交换机端口配置的方法
    def interface_conf(self):
        pass



if __name__ == '__main__':
    path = os.getcwd()
    if not os.path.exists(path + 'info.csv'):
        f = open(path + 'info.csv', 'w', newline='')


