from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Base(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        abstract = True


class Category(Base):
    name = models.CharField(verbose_name="名称", max_length=100, unique=True)
    description = models.TextField(verbose_name="描述", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "类别"


class Article(Base):
    user = models.ForeignKey(User, verbose_name="用户", related_name="user")
    title = models.CharField(verbose_name="标题", max_length=255)
    content = models.TextField(verbose_name="内容")
    # 删除category之前要先删除article,(默认情况下删除category会级联删除article)
    category = models.ForeignKey(Category, verbose_name="类别", on_delete=models.PROTECT, related_name="articles")
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ("-create_time", )
