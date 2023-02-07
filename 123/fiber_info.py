#脚本作者:胡克超
#日期:2022-5-22

from email import header
from telnetlib import Telnet
import time,re,sys,csv,multiprocessing
from concurrent.futures import ProcessPoolExecutor, process
class Switch():
    def __init__(self,host=None,username=None,password=None,enable=''):
        self.host = host
        self.username = username
        self.password = password
        self.enable = enable
        #connected:Telnet成功为True,否则为False
        self.connected = False
        #switch_name:交换机名称
        self.switch_name=None
        #brand:设备品牌{Cisco,HuaWei,H3C}
        self.brand=False
        #交换机进入到全局模式下名称后的标识符(cisco-'#';huawei-']';H3C-']')
        self.tag=']'
        #self.tn:Telnet对象
        # self.tn=None
        self.tn=None
        # self.login()
        self.error_txt=''

    def login(self):
        try:
            #try成功置connected为True
            self.tn=Telnet(self.host,port=23,timeout=3)
            self.connected=True
        except:
            #否则表示Telnet失败
            self.connected=False
            self.error_txt=self.host+',Telnet失败\n'
            print(self.error_txt)

        #Telnet成功,下一步输入账号密码,通过返回字段区分交换机类型
        if self.connected:

            get_login_word=self.tn.read_until(b":",timeout=3)
            get_login_word=get_login_word.decode()
            self.tn.write(self.username.encode('ascii')+b'\n')
            self.tn.read_until(b"assword:",timeout=3)
            self.tn.write(self.password.encode('ascii')+b'\n')
            #如果返回信息账号提示词为loging:则区分为H3C交换机
            if 'login:' in get_login_word or 'Login' in get_login_word:
                self.brand='H3C'
                #如果账号需要提权则输入super
                if self.enable!='':
                    self.tn.write('super'.encode('ascii')+b'\n')
                    self.tn.read_until(b"assword:",timeout=3)
                    self.tn.write(self.enable.encode('ascii')+b'\n')

                self.tn.read_until(b">",timeout=3)
                #H3C设备取消分页,便于一次性返回信息
                self.tn.write('screen-length disable'.encode('ascii')+b'\n')
                self.tn.write('system-view'.encode('ascii')+b'\n')
                get_info=self.tn.read_until(b"]",timeout=3)
                get_info=get_info.decode()
                get_h3c_name=re.findall(r'\[(.*)\]',get_info)
                if get_h3c_name:
                   self.switch_name=get_h3c_name[0]

            else:

                get_left_word=self.tn.read_until(b">",timeout=3)
                get_left_word=get_left_word.decode()
                #获取包含交换机名的最后一行信息内容
                get_last_str=re.split(r'\n',get_left_word)[-1]
                re_huawei_name=re.findall(r'^<(.*)>$',get_last_str)

                #HUAWEI设备
                if re_huawei_name:
                    self.brand='HuaWei'
                    self.switch_name=re_huawei_name[0]
                    if self.enable!='':
                        self.tn.write('super'.encode('ascii')+b'\n')
                        self.tn.read_until(b"assword:",timeout=3)
                        self.tn.write(self.enable.encode('ascii')+b'\n')
                    self.tn.read_until(b">",timeout=3)
                    self.tn.write('screen-length 0 temporary'.encode('ascii')+b'\n')
                    self.tn.read_until(b">",timeout=3)
                    self.tn.write('system-view'.encode('ascii')+b'\n')
                    self.tn.read_until(b"]",timeout=3)


                #Cisco设备
                else:
                    re_cisco_name=re.findall(r'^(.*)>$',get_last_str)

                    if re_cisco_name:
                        self.brand='Cisco'
                        self.switch_name=re_cisco_name[0]
                        self.tag='#'

                    if self.enable!='':
                        self.tn.write('enable'.encode('ascii')+b'\n')
                        self.tn.read_until(b"assword:",timeout=3)
                        self.tn.write(self.enable.encode('ascii')+b'\n')
                        self.tn.read_until(b"#",timeout=3)
                        self.tn.write('terminal length 0'.encode('ascii')+b'\n')
                        self.tn.read_until(b"#",timeout=3)
                    else:
                        self.tag='>'
                        self.tn.write('terminal length 0'.encode('ascii')+b'\n')
                        self.tn.read_until(b">",timeout=3)

        return self.tn


    def cmd_message(self,cmd):
        """
        向交换机发送命令并返回信息
        cmd:发送的命令
        return:返显文本内容
        """
        return_txt=''
        if self.connected:
            if self.brand=='Cisco' and self.enable=='':
                self.tag='>'
            self.tn.write(cmd.encode('ascii')+b'\n')
            if '|' in cmd:
                cmd=cmd.replace('|','\|')
            if '^' in cmd:\
                cmd=cmd.replace('^','\^')
            rex_content=cmd+'([\S\s]*)'+'[^@]'+self.switch_name+self.tag
            # print(rex_content)
            while True:
                time.sleep(0.5)
                info=self.tn.read_very_eager()
                # print(info)
                return_txt+=str(info.decode())
                rex=re.findall(rex_content,return_txt)
                # print(return_txt)
                if rex:
                    return_txt=rex[0]
                    break
        return return_txt

    def check_sfp_info(self):
        """
        查询交换机光模块信息方法
        """
        if self.tn:

            return_list=list()

            if self.brand=='Cisco':
                cmd_return=self.cmd_message('show inventory')

                get_re_str=re.findall('NAME: \"(.*)\", DESCR: \"(.*)\"\r\n, PID:(.*?),.*SN:(.*)',cmd_return)

                if len(get_re_str)>1:
                    for info in get_re_str[1:]:
                        temp_dict={
                            'ip':self.host,
                            'name':self.switch_name,
                            'brand':self.brand,
                            'port':'',
                            'descr':'',
                            'mode':'',
                            'sn':''
                        }
                        port=info[0].strip()
                        #跳过Cisco-3850的电源模块信息
                        if 'Switch' in port:
                            continue
                        temp_dict['port']=port
                        temp_dict['descr']=info[1].strip()
                        temp_dict['mode']=info[2].strip()
                        temp_dict['sn']=info[3].strip()
                        return_list.append(temp_dict)
                    print(str(self.host)+':查询完毕\n')


            if self.brand=='HuaWei':
                cmd_return=self.cmd_message('display transceiver')
                get_re_str=re.findall('(.*)transceiver information[\S\s]*?Transceiver Type.*:(.*)[\S\s]*?Connector Type.*:(.*)[\S\s]*?Wavelength.*:(.*)[\S\s]*?Serial Number.*:(.*)',cmd_return)
                if get_re_str:
                    for info in get_re_str:
                        temp_dict={
                                'ip':self.host,
                                'name':self.switch_name,
                                'brand':self.brand,
                                'port':'',
                                'descr':'',
                                'mode':'',
                                'sn':''
                            }
                        temp_dict['port']=info[0].strip()
                        temp_dict['descr']=info[1].strip()
                        mode_str='SFP-'+info[2].strip()+'-'+info[3].strip()
                        temp_dict['mode']=mode_str
                        temp_dict['sn']=info[4].strip()
                        return_list.append(temp_dict)
                    print(str(self.host)+':查询完毕\n')

            if self.brand=='H3C':
                cmd_return=self.cmd_message('dis transceiver interface')
                get_re_str=re.findall('(.*)transceiver information:.*\n.*Transceiver Type.*:(.*)[\S\s]*?Ordering Name.*:(.*)[\S\s]*?Serial Number.*:(.*)',cmd_return)
                if get_re_str:
                    for info in get_re_str:

                        temp_dict={
                                'ip':self.host,
                                'name':self.switch_name,
                                'brand':self.brand,
                                'port':'',
                                'descr':'',
                                'mode':'',
                                'sn':''
                            }

                        port=info[0].strip()
                        temp_dict['sn']=info[3].strip()
                        get_sn_txt=self.cmd_message('display transceiver manuinfo interface '+port)
                        get_sn=re.findall('Serial Number :(.*)',get_sn_txt)
                        if get_sn:
                            temp_dict['sn']=get_sn[0].strip()
                        temp_dict['port']=port
                        temp_dict['descr']=info[1].strip()
                        temp_dict['mode']=info[2].strip()

                        return_list.append(temp_dict)
                    print(str(self.host)+':查询完毕\n')


            if return_list:
                return return_list

            else:
                no_info=str(self.host)+',无模块信息或查询异常\n'
                print(no_info)
                return no_info


    def close_connected(self):
        """
        断开Telent连接
        """
        if self.tn:
            self.tn.close()


def do(ip,username,password,enable):
    do_return={
        'error':'',
        'info':None
    }
    tn=Switch(host=ip,username=username,password=password,enable=enable)
    tn.login()
    if tn:
        do_return['error']=tn.error_txt
        get_sfp_info=tn.check_sfp_info()
        # print(get_sfp_info)
        do_return['info']=get_sfp_info
        tn.close_connected()

    return do_return

def process_result(obj):
    """
    收集进程返回结果
    """
    result_list.append(obj.result())


def process_pool(ip_list,username,password,enable):
    with ProcessPoolExecutor(max_workers=int(process_a)) as executor:

        for ip in ip_list:
            ip=ip.strip()
            if ip=='':
                continue
            executor.submit(do,ip,username,password,enable).add_done_callback(process_result)

        executor.shutdown(wait=True)

if __name__ == "__main__":
    global result_list
    global process_a
    process_a=10
    result_list=list()
    multiprocessing.freeze_support()
    #读取IP表
    ip_list=list()
    try:
        with open('ip.txt','r') as ip_obj:
           ip_list =ip_obj.readlines()
    except:
        input('读取ip.txt文件数据出错')
        sys.exit(0)

    #读取进程数量和登录信息
    login_txt=''
    try:
        with open('login.txt','r') as login_obj:
            login_txt=login_obj.read()
    except:
        input('读取login.txt文件数据出错')
        sys.exit(0)


    if login_txt!='':

        try:
            username=re.findall('username=(.*)',login_txt)[0].strip()
            password=re.findall('password=(.*)',login_txt)[0].strip()
            enable=re.findall('enable=(.*)',login_txt)[0].strip()

            process_a=re.findall('process=(.*)',login_txt)[0].strip()
        except:
            input('读取login.txt文件参数识别出错')
            sys.exit(0)

        #执行多进程函数
        csv_result=list()

        get_error_log=''

        process_pool(ip_list,username,password,enable)

        for a_list in result_list:
            if '失败' in a_list['error']:
                get_error_log+=a_list['error']

            elif  '异常' in a_list['info']:
                get_error_log+=a_list['info']

            else:
                csv_result+=a_list['info']


        log_name='失败日志.txt'
        while True:
            try:
                with open(log_name,'w') as error_obj:
                    error_obj.write(get_error_log)
                break
            except:
                log_name='失败日志'+str(int(time.time()))+'.txt'

        csv_result=[{'ip':'交换机IP','name':'交换机名称','brand':'品牌','port':'端口号','descr':'模块速率','mode':'模块接口类型','sn':'模块SN'}]+csv_result
        csv_name='交换机模块信息.csv'

        while True:
            try:
                f_name=['ip','name','brand','port','descr','mode','sn']
                with open(csv_name,'w',newline='') as csv_obj:
                    writer=csv.DictWriter(csv_obj,fieldnames=f_name)
                    writer.writerows(csv_result)
                break
            except:
                csv_name='交换机模块信息'+str(int(time.time()))+'.csv'



