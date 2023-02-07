import telnetlib


class Huawei_switch:
    def __init__(self):
        self.tag = None
        self.switch_name = None
        self.enable = None
        self.brand = None
        self.error_txt = None
        self.connected = None
        self.tn = None
        self.host = None
        self.password = None

    def login(self):
        try:
            # try成功置connected为True
            self.tn = telnetlib.Telnet(self.host, port=23, timeout=3)
            self.connected = True
        except:
            # 否则表示Telnet失败
            self.connected = False
            self.error_txt = self.host + ',Telnet失败\n'
            print(self.error_txt)
            # Telnet成功,下一步输入账号密码,通过返回字段区分交换机类型
            if self.connected:

                get_login_word = self.tn.read_until(b":", timeout=3)
                get_login_word = get_login_word.decode()
                self.tn.write(self.username.encode('ascii') + b'\n')
                self.tn.read_until(b"assword:", timeout=3)
                self.tn.write(self.password.encode('ascii') + b'\n')
                # 如果返回信息账号提示词为loging:则区分为H3C交换机
                if 'login:' in get_login_word or 'Login' in get_login_word:
                    self.brand = 'H3C'
                    # 如果账号需要提权则输入super
                    if self.enable != '':
                        self.tn.write('super'.encode('ascii') + b'\n')
                        self.tn.read_until(b"assword:", timeout=3)
                        self.tn.write(self.enable.encode('ascii') + b'\n')

                    self.tn.read_until(b">", timeout=3)
                    # H3C设备取消分页,便于一次性返回信息
                    self.tn.write('screen-length disable'.encode('ascii') + b'\n')
                    self.tn.write('system-view'.encode('ascii') + b'\n')
                    get_info = self.tn.read_until(b"]", timeout=3)
                    get_info = get_info.decode()
                    get_h3c_name = re.findall(r'\[(.*)\]', get_info)
                    if get_h3c_name:
                        self.switch_name = get_h3c_name[0]

                else:

                    get_left_word = self.tn.read_until(b">", timeout=3)
                    get_left_word = get_left_word.decode()
                    # 获取包含交换机名的最后一行信息内容
                    get_last_str = re.split(r'\n', get_left_word)[-1]
                    re_huawei_name = re.findall(r'^<(.*)>$', get_last_str)

                    # HUAWEI设备
                    if re_huawei_name:
                        self.brand = 'HuaWei'
                        self.switch_name = re_huawei_name[0]
                        if self.enable != '':
                            self.tn.write('super'.encode('ascii') + b'\n')
                            self.tn.read_until(b"assword:", timeout=3)
                            self.tn.write(self.enable.encode('ascii') + b'\n')
                        self.tn.read_until(b">", timeout=3)
                        self.tn.write('screen-length 0 temporary'.encode('ascii') + b'\n')
                        self.tn.read_until(b">", timeout=3)
                        self.tn.write('system-view'.encode('ascii') + b'\n')
                        self.tn.read_until(b"]", timeout=3)


                    # Cisco设备
                    else:
                        re_cisco_name = re.findall(r'^(.*)>$', get_last_str)

                        if re_cisco_name:
                            self.brand = 'Cisco'
                            self.switch_name = re_cisco_name[0]
                            self.tag = '#'

                        if self.enable != '':
                            self.tn.write('enable'.encode('ascii') + b'\n')
                            self.tn.read_until(b"assword:", timeout=3)
                            self.tn.write(self.enable.encode('ascii') + b'\n')
                            self.tn.read_until(b"#", timeout=3)
                            self.tn.write('terminal length 0'.encode('ascii') + b'\n')
                            self.tn.read_until(b"#", timeout=3)
                        else:
                            self.tag = '>'
                            self.tn.write('terminal length 0'.encode('ascii') + b'\n')
                            self.tn.read_until(b">", timeout=3)

            return self.tn
    def cmd_message(self, cmd):
        """
        向交换机发送命令并返回信息
        cmd:发送的命令
        return:返显文本内容
        """
        return_txt = ''
        if self.connected:
            if self.brand == 'Cisco' and self.enable == '':
                self.tag = '>'
            self.tn.write(cmd.encode('ascii') + b'\n')
            if '|' in cmd:
                cmd = cmd.replace('|', '\|')
            if '^' in cmd: \
                    cmd = cmd.replace('^', '\^')
            rex_content = cmd + '([\S\s]*)' + '[^@]' + self.switch_name + self.tag
            # print(rex_content)
            while True:
                time.sleep(0.5)
                info = self.tn.read_very_eager()
                # print(info)
                return_txt += str(info.decode())
                rex = re.findall(rex_content, return_txt)
                # print(return_txt)
                if rex:
                    return_txt = rex[0]
                    break
        return return_txt



