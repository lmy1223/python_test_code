# -*- coding: utf-8 -*-
# 简单的发邮件测试

import yagmail
# user = 'moon_1223@163.com'
# password = 'nicai?'

yag = yagmail.SMTP(user='moon_1223@163.com', password='nicai?', host='smtp.163.com', port='25')
yag.send(to="lmy@mingyueli.com", subject="I now can send an attachment", contents='contents')

# def main():
#     yag = yagmail.SMTP(user, password, host="smtp.163.com", port="25")
#     subject = "This is system info"
#     content = "This is a test"
#     yag.send(yag.user, subject=subject, contents=content, smtp_starttls=False, smtp_skip_login=True)
#     my = mail_user('moon_1223@163.com', 'nicai?')
#     my.send_mail()
#
#
# if __name__ == '__main__':
#     main()

