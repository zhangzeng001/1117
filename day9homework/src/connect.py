import paramiko
import optparse
import configparser
from conf import settings

# def conn():
#     print(settings.ACCOUNT_FILE)
#     config = configparser.ConfigParser()
#     config.read(settings.ACCOUNT_FILE)
#     res = config.sections()
#     print(res)

class SSH_client:
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-o","--host",dest="hostname",help='Please input your hostname')
        parser.add_option("-g","--group",dest="group",help='Please input your group')
        parser.add_option("-m","--cmd",dest="cmd",help='Please input your cmd')
        self.options,self.args = parser.parse_args()
        #校验参数，执行命令
        self.verify_args(self.options,self.args)

    def verify_args(self,options,args):
        if options.hostname and options.group :
            print("传参错误！")
        if options.cmd is None:
            print('-m or --cmd 输入命令！')
        if options.hostname:
            self.conn_ssh(options.hostname,options.cmd)
        else:
            #options.group
            pass


    def conn_ssh(self,hostname,cmd):
        print(hostname,"=====>",cmd)
        # 创建ssh对象
        ssh = paramiko.SSHClient()
        #允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        #连接服务器
        ssh.connect()











