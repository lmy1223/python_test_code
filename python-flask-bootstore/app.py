#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

# import time

import pymysql
from flask import (Flask, render_template, g, session, redirect, url_for,
                   request, flash)
from flask_bootstrap import Bootstrap

from forms import InsertBookListForm, ModifyBookListForm

SECRET_KEY = 'key'

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = SECRET_KEY
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'admin'


def connect_db():
    """Returns a new connection to the database."""
    return pymysql.connect(host='127.0.0.1',
                           user='root',
                           passwd='123',
                           db='test',
                           charset="utf8")


@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    g.db = connect_db()


@app.after_request
def after_request(response):
    """Closes the database again at the end of the request."""
    g.db.close()
    return response


@app.route('/', methods=['GET', 'POST'])
def show_book_list():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    form = InsertBookListForm()
    if request.method == 'GET':
        sql = 'select id, user_id, book_name, book_price, create_time from bookstore'
        with g.db as cur:
            cur.execute(sql)
            book_list = [dict(id=row[0], user_id=row[1], book_name=row[2], book_price=row[3], create_time=row[4]) for
                         row in cur.fetchall()]
        return render_template('index.html', book_list=book_list, form=form)
    else:
        if form.validate_on_submit():
            book_name = form.book_name.data
            book_price = form.book_price.data
            # a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            with g.db as cur:
                sql = """insert into bookstore(`user_id`, `book_name`, `book_price`
                ) values ({0}, '{1}', {2})""".format(1, book_name, book_price)
                cur.execute(sql)
            flash('添加了一本图书 ！')
        else:
            flash(form.errors)
        return redirect(url_for('show_book_list'))


@app.route('/delete')
def delete_book_list():
    id = request.args.get('id', None)
    if id is None:
        abort(404)
    else:
        sql = "delete from bookstore where id = {0}".format(id)
        with g.db as cur:
            cur.execute(sql)
        flash('删除了一本书 ！')
        return redirect(url_for('show_book_list'))


@app.route('/modify', methods=['GET', 'POST'])
def modify_book_list():
    id = request.args.get('id', None)
    form = ModifyBookListForm()
    if request.method == 'GET':
        sql = 'select id, user_id, book_name, book_price, create_time from bookstore'
        with g.db as cur:
            cur.execute(sql)
            book_list = [dict(id=row[0], user_id=row[1], book_name=row[2], book_price=row[3], create_time=row[4]) for
                         row in cur.fetchall()]
        return render_template('modify.html', book_list=book_list, form=form)
    else:
        if form.validate_on_submit():
            # id = request.args.get('id', None)
            book_name = form.book_name.data
            book_price = form.book_price.data
            # a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            sql = "update bookstore set book_name = '{0}', book_price = {1} where id = {2}".format(book_name, book_price, id)
            with g.db as cur:
                cur.execute(sql)
            flash('修改了一本书 ！')
        else:
            flash(form.errors)
        return redirect(url_for('show_book_list'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('请输入正确的用户名 ！')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('请输入正确的密码 ！')
        else:
            session['logged_in'] = True
            flash('成功登录系统 !')
            return redirect(url_for('show_book_list'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('成功登出系统 !')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
