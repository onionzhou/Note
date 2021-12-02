import subprocess
import os


# cmd1 = "cd /etc/ld.so.conf.d"
# cmd = "cd /etc/ld.so.conf.d;ls -lrt  | grep  'dbappsecurity.conf.' |grep -v 'dbappsecurity.conf.failed' | awk '{print $NF}'"
# #
# ret = os.popen(cmd1).read()
# print(ret)
# ret = os.popen(cmd).read().strip()
# print(ret)
# # ret_list = ret.split()
# # upload_file = ret_list[-1]

def check():
    keep_file=1 #
    path = '/etc/ld.so.conf.d'
    cur_dir = os.getcwd()
    os.chdir(path)
    files = os.listdir('./')
    files_list = sorted(files, key=lambda x: os.path.getmtime(os.path.join(path, x)))  #
    tmp_list = []
    for name in files_list:
        if 'dbappsecurity.conf.failed' == name:
            continue
        if 'dbappsecurity.conf.' in name:
            tmp_list.append(name)

    print(tmp_list)

    dir_list =[]
    if (len(tmp_list) > keep_file):
        for del_name in tmp_list[:-keep_file]:
            suffix=del_name.split('.')[-1]
            dir_list.append('dbappsecurity.'+suffix)
            os.remove(del_name)

    os.chdir(cur_dir)

    os.chdir('/opt')
    for del_name in dir_list:
        try:
            os.system('rm -rf {}'.format(del_name))
        except:
            pass
    os.chdir(cur_dir)


if __name__ == '__main__':
    check()
