# -*- coding: UTF-8 -*-


import MySQLdb


class MySQLUtil:

    def __init__(self, dbHost='localhost', dbUser='lgbaccess', dbPass='lgbaccess', dbName='lgb_access', dbPort=3306):
        self.conn = MySQLdb.connect(host=dbHost, user=dbUser, passwd=dbPass, db=dbName, port=dbPort)

    def insert(self, sql, args):
        # 获得链接
        cur = self.conn.cursor()
        # 执行插入操作
        cur.execute(sql, args)
        # 提交事务
        self.conn.commit()

    def select(self, sql, *args):
        # 获得链接
        cur = self.conn.cursor()
        # 执行插入操作
        cur.execute(sql, *args)
        # 提交事务
        self.conn.commit()
        return cur.fetchall()

    def update(self, sql, *args):
        # 获得链接
        cur = self.conn.cursor()
        # 执行插入操作
        cur.execute(sql, *args)
        # 提交事务
        self.conn.commit()
