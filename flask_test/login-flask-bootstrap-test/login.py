# -*- coding: UTF-8 -*-

# from contextlib import closing
# from __future__ import unicode_literals
#
# import time

from flask import (Flask, render_template, g, session, redirect, url_for,
                   request, flash)
from flask_bootstrap import Bootstrap

DEBUG = True
SECRET_KEY = 'This is my key'

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.secret_key = SECRET_KEY
app.config.from_object(__name__)
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'admin'


@app.route('/login')
def hello_world():
    return render_template('hello.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('hello_world'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return render_template('logout.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1")
