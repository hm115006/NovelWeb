# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Chapter(models.Model):
    novelid = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
    sort = models.CharField(max_length=100)
    chapterid = models.IntegerField()
    title = models.CharField(primary_key=True, max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chapter'


class ChapterCopy(models.Model):
    novelid = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
    sort = models.CharField(max_length=100)
    chapterid = models.IntegerField()
    title = models.CharField(primary_key=True, max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chapter_copy'


class ChapterCopy1(models.Model):
    name1 = models.CharField(max_length=100)
    chapterid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chapter_copy1'


class Chaptertest(models.Model):
    novelid = models.IntegerField()
    name1 = models.CharField(max_length=100)
    sort = models.CharField(max_length=100)
    chapterid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'chaptertest'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Novel(models.Model):
    novelid = models.CharField(primary_key=True, max_length=100)
    sort = models.CharField(max_length=20)
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'novel'


class NovelCopy(models.Model):
    novelid = models.CharField(primary_key=True, max_length=100)
    sort = models.CharField(max_length=20)
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'novel_copy'


class NovelCopy1(models.Model):
    novelid = models.AutoField(primary_key=True)
    sort = models.CharField(max_length=20)
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'novel_copy1'


class Noveltest(models.Model):
    novelid = models.IntegerField(primary_key=True)
    sort = models.CharField(max_length=20)
    novelname = models.CharField(max_length=100)
    novelimg = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'noveltest'
