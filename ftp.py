import paramiko
import time
 
def ftp():
    #创建ssh对象
    ssh = paramiko.SSHClient()
    #ssh.load_host_keys("C:/Users/Administrator/.ssh/known_hosts")
    #允许连接不在know_hosts文件的主机上
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    filename = ['data.txt']
    #本地文件路径
    for i in filename:
        localpath = i
    #服务器的文件路径
        remotepath = "/root/Web/files/" + i
    #可设置多台服务器，尽量服务器的密码保持一致
        server = "8.130.14.17"
    # words = server.split(",")
    # for word in words:
      #连接服务器
        print(server,'开始数据传输')
        ssh.connect(server, username="root", password="a.59304681")
        sftp = ssh.open_sftp()
        sftp.put(localpath, remotepath, callback = None)
        #关闭连接
        ssh.close()
        print('数据传输完成')
        time.sleep(1)