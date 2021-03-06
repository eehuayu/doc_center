# coding: utf-8

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Base(models.Model):
    create_time = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(verbose_name=u"名称", max_length=100, unique=True)
    description = models.TextField(verbose_name=u"描述", null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = u"类别"


class Article(Base):
    title = models.CharField(verbose_name=u"标题", max_length=255, unique=True)
    content = models.TextField(verbose_name=u"内容", )
    # 删除category之前要先删除article,(默认情况下删除category会级联删除article)
    category = models.ForeignKey(Category, verbose_name=u"类别", on_delete=models.PROTECT, related_name="articles")
    update_time = models.DateTimeField(verbose_name=u"更新时间", auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = u"文章"
        ordering = ("-create_time", )


class UploadFile(Base):
    title = models.CharField(verbose_name=u"标题", max_length=255, unique=True)
    my_file = models.FileField(verbose_name=u"文件", upload_to='upload')
    desc = models.CharField(verbose_name=u"描述", max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = u"文件"
