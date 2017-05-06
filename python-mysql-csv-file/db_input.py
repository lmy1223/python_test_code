#!/usr/bin/python
# -*- coding: UTF-8 -*-
# This is a script that writes data from CSV to MySQL

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

    # 创建数据表
    cur.execute("DROP TABLE IF EXISTS `student`")
    conn.commit()
    create_db = """create table student(
                    id int,
                    name varchar(10),
                    sex char(4),
                    age int
                    )
                   ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cur.execute(create_db)
    conn.commit()

    # 读一个 CSV file 到一个数组里
    f = open("input_CSV_file.csv", 'r')
    student = []
    for row in csv.reader(f):
        student.append(row)
    f.close()

    # 还可以替换成为with
    # student = []
    # with open("input_CSV_file.csv", 'r') as f:
    #     for row in csv.reader(f):
    #         student.append(row)

    # 执行 insert
    insert_db = "insert into student values(%s, %s, %s, %s)"
    cur.executemany(insert_db, student)
    conn.commit()

    # 关闭连接
    if cur:
        cur.close()
    if conn:
        conn.close()


if __name__ == '__main__':
    main()
