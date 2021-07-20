import paramiko
import re
import time
import argparse
import select


class SSH_CON_API():

    def __init__(self, ip, port, username, passwd):
        self.ip = ip
        self.port = port
        self.username = username
        self.passwd = passwd

    def ssh_connect(self):
        trans = paramiko.Transport((self.ip, self.port))
        trans.start_client()
        trans.auth_password(username=self.username, password=self.passwd)
        channel = trans.open_session()
        channel.get_pty()
        channel.invoke_shell()
        channel.settimeout(3)

        chn = channel

        # 登录运维主机
        p = re.compile(r'~]*')
        while True:
            ret = chn.recv(2048).decode('UTF-8')
            print(ret)
            if p.search(ret):
                # 成功登陆线程，写入其id
                break
            time.sleep(2)

        return chn

    def sftp_connect(self):
        try:
            trans = paramiko.Transport((self.ip, self.port))
            trans.connect(username=self.username, password=self.passwd)
            sftp = paramiko.SFTPClient.from_transport(trans)
            print(sftp.listdir())
        except Exception as e:
            print(e)
        return sftp

    def upload_file(self, sftp, local, remote):
        try:
            sftp.put(local, remote)
        except Exception as e:
            print(e)
            sftp.close()

    def close(self, sftp):
        sftp.close()

    def send_cmd(self, chn, cmd):
        chn.send(cmd + '\r')
        time.sleep(1)

        while True:
            ret = chn.recv(2048).decode('UTF-8')
            print(ret)
            print(len(ret))
            if ret == 0:
                break

    def ssh_tmp_test(self, cmd):
        client = paramiko.SSHClient()
        # client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(self.ip, self.port, self.username, self.passwd)
        _, ss_stdout, ss_stderr = client.exec_command(cmd)
        time.sleep(2)
        # while not ss_stdout.channel.exit_status_ready():
        #     if ss_stdout.channel.recv_ready():
        #         rl, wl, xl = select.select([ss_stdout.channel], [], [], 0.0)
        #         if len(rl) > 0:
        #             print(ss_stdout.channel.recv(1024).decode('utf-8'))

        while True:
            ret = ss_stdout.readlines()
            new_list=list(set(ret))
            new_list.sort(key=ret.index)

            print(len(ret))
            print(new_list)
            print('--------去重前------------')
            for i in ret:
                print(i)
            print('hhhhhhhhhhhhhhhhhhhhhhhhhhh')
            print('-----------去重后的------------')
            for i in new_list:
                print(i)
            print('hhhhhhhhhhhhhhhhhhhhhhhhhhh')
            if len(ret) == 0:
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-host', type=str)
    parser.add_argument('-port', type=str)
    parser.add_argument('-u', type=str)
    parser.add_argument('-p', type=str)
    parser.add_argument('-cmd', type=str)

    args = parser.parse_args()

    ip = args.host
    port = int(args.port)

    username = args.u
    passwd = args.p

    cmd = 'bash rollback.sh'

    print(ip, port, username, passwd)
    print(type(ip), type(port), type(username), type(passwd))
    ssh_con = SSH_CON_API(ip, port, username, passwd)

    sftp = ssh_con.sftp_connect()
    ssh_con.upload_file(sftp, 'rollback.sh', '/root/rollback.sh')
    ssh_con.close(sftp)

    # chn = ssh_con.ssh_connect()
    # ssh_con.send_cmd(chn, cmd)
    ssh_con.ssh_tmp_test(cmd)
