#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField
from wtforms.validators import DataRequired, Length


class InsertBookListForm(FlaskForm):
    book_name = StringField('图书名称', validators=[DataRequired(), Length(1, 64)])
    book_price = StringField('图书价格', validators=[DataRequired()] )
    submit = SubmitField('添加')


class ModifyBookListForm(FlaskForm):
    book_name = StringField('图书名称', validators=[DataRequired(), Length(1, 64)])
    book_price = StringField('图书价格', validators=[DataRequired()] )
    submit = SubmitField('修改')
