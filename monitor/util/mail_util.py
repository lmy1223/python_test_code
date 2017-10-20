# -*- coding: utf-8 -*-


import yagmail


class MailUtil:

    def __init__(self, user, password, server_host, server_port):
        self.user = user
        self.password = password
        self.server_host = server_host
        self.server_port = server_port

    def send_mail(self, body, subject, to_user):
        yag = yagmail.SMTP(self.user, self.password, self.server_host, self.server_port)
        yag.send(to=to_user, subject=subject, contents=body)
