# -*- coding: utf-8 -*-

from util.HttpStatusUtil import HttpStatusUtil
from util.mail_util import MailUtil
from util.message_util import MessageUtil
from util.mysql_util import MySQLUtil
import time
import uuid
import json
import re

running = True


class LgbMenhuMonitor:

    def __init__(self):
        return

    def monitor_and_send_message(self):
        http_url = "http://baidu.com"
        status_util = HttpStatusUtil(http_url)
        response = status_util.get_http_status_response()
        status_code = response.get("status_code")
        status_information = response.get("status_information")

        # 控制开关
        mysql_util = MySQLUtil(
            dbHost="localhost",
            dbUser="lgbaccess",
            dbPass="lgbaccess",
            dbName="lgb_access",
            dbPort=3306
        )
        select_sql = "SELECT running FROM `config` WHERE `id` ='1'"
        running_tuple = mysql_util.select(sql=select_sql)
        for n in running_tuple:
            for m in n:
                if m == 1:
                    if not (re.match(r'^2', str(status_code)) or re.match(r'^3', str(status_code))):
                        print "something is wrong"
                        update_sql = "UPDATE `config` SET `running`='0' WHERE `id`='1'"
                        mysql_util.update(sql=update_sql)
                        # 向数据库插入这次记录信息
                        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        args = (status_code, status_information, now_time)
                        sql = "INSERT INTO information(statusCode,statusInformation,nowTime) VALUES(%s, %s, %s)"

                        mysql_util.insert(sql=sql, args=args)

                        # 向管理员发送短信
                        message_util = MessageUtil()
                        business_id = uuid.uuid1()
                        send_msg = {
                            "now_time": now_time,
                            "status_code": status_code,
                            "status_information": status_information
                        }
                        params = json.dumps(send_msg)
                        print message_util.send_sms(business_id, "13795108621", "竹林科技", "SMS_103340052", params)

                        # 向管理员发送邮件
                        mail_util = MailUtil(
                            user="XXX@163.com",
                            password="XXXX",
                            server_host="smtp.163.com",
                            server_port=25
                        )

                        body = """
                               Dear :

                                   下面是{0}发送的对网站 "{3}" 检测到的错误信息：

                               状态码：{1}
                               状态信息: {2}
                               发送时间：{0}
                                   """.format(now_time, status_code, status_information, http_url)
                        subject = """
                                服务器监控邮件提醒
                            """
                        mail_util.send_mail(body=body, subject=subject, to_user="xxxx@qq.com")

                        # 关闭连接
                        if mysql_util.conn:
                            mysql_util.conn.close()
                    else:
                        print "normal"
                        update_sql = "UPDATE `config` SET `running`='1' WHERE `id`='1'"
                        mysql_util.update(sql=update_sql)
                elif m == 0:
                    print "normal"
                    if re.match(r'^2', str(status_code)) or re.match(r'^3', str(status_code)):
                        update_sql = "UPDATE `config` SET `running`='1' WHERE `id`='1'"
                        mysql_util.update(sql=update_sql)
