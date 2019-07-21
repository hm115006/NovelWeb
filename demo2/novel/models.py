# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from mongoengine import *
from django.db import models

class novel_info(Document):
    # 定义数据库中的所有字段
    _id = IntField(primary_key=True)
    sort = StringField()
    name = StringField()
    author = StringField()
    status = StringField()
    description = StringField()
    img = StringField()
    novelid = IntField()
    # 指明连接的数据表名
    meta = {'collection': 'novel_info'}


class chapter_info(Document):
    _id = IntField()
    novelid = IntField()
    novelnane = StringField()
    sort = StringField()
    order_id = IntField()
    chapter_name = StringField()
    chapter_content = StringField()
    meta = {'collection': 'chapter_info'}
