#!/usr/bin python
# -*- coding: utf-8 -*-
# 收集简单服务器信息并发送邮件

import yagmail
import psutil
import os


class mail_user:
    def __init__(self, user, password, host='smtp.163.com', port="25"):
        self.port = port
        self.host = host
        self.user = user
        self.password = password

    def send_mail(self, dict_file):
        yag = yagmail.SMTP(self.user, self.password, self.host, self.port)
        subject = "This is system info"
        yag.send(to="lmy@mingyueli.com", subject=subject, contents=dict_file)


def get_new_file():
    os.system("touch {0}".format('/usr/local/python_test/systemInfo'))


def get_system_info_to_file():
    os.chdir(r'/usr/local/python_test/')
    a = psutil.cpu_count()
    b = psutil.cpu_percent()  # cpu利用率，监控实时变化的
    c = psutil.virtual_memory()
    d = psutil.disk_usage('/usr/local/').percent
    global dict_file
    dict_file = {'cpu_count': a, 'cpu_percent': b, 'virtual_memory': c, 'disk_usage': d}
    # with os.open('/usr/local/python_test/systemInfo', 'w') as f:
    #     for key in dict_file:
    #         f.write(key)
    #     # f.writelines(a, b, c, d)
    # return f
    # for line in open("systemInfo"):
    #     print line
    #     lines = line.rstrip()

    # f.close()


def main():
    get_new_file()
    get_system_info_to_file()
    my = mail_user('moon_1223@163.com', 'nicai?')
    my.send_mail(dict_file)


if __name__ == '__main__':
    main()
