# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from  datetime import datetime
from django.db import models

# Create your models here.

from  users.models import UserProfile
from  courses.models import  Course
from  organization.models import  Teacher
from  yyonline import settings

class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"姓名")
    mobile = models.CharField(max_length=11,verbose_name=u"手机")
    course_name = models.CharField(max_length=50,verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u"用户名")
    course = models.ForeignKey(Course,verbose_name=u"课程名")
    comments = models.CharField(max_length=200,verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

    # def __unicode__(self):
    #     return self.name

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"用户名")
    fav_id = models.IntegerField(default=0,verbose_name=u"数据ID")
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"机构"),(3,"教练")),verbose_name=u"收藏类型")

    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u"接受用户")
    message =  models.CharField(max_length=200,verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False,verbose_name=u"是否已读")#False 未读
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    # def __unicode__(self):
    #     return self.name

class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"学习时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

    # def __unicode__(self):
    #     return self.name