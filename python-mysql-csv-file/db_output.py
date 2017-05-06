#!/usr/bin/python
# -*- coding: UTF-8 -*-
# This is a script that writes data from MySQL to csv

import csv
import MySQLdb


def main():
    # 连接数据库
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123',
        db='test',
    )
    cur = conn.cursor()

    # 以写的方式打开 csv 文件
    f = open("output_CSV_file.csv", 'w')
    w = csv.writer(f)

    # 从 student 表里面读出数据，写入到 csv 文件里
    cur.execute("select * from student")
    while True:
        row = cur.fetchone()
        if not row:
            break
        w.writerow(row)
    f.close()

    # 关闭连接
    if cur:
        cur.close()
    if conn:
        conn.close()


if __name__ == '__main__':
    main()
