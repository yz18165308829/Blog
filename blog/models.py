from datetime import datetime

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse

"""
Django 内置的全部类型可查看文档:https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
"""


class Category(models.Model):
    """分类表"""
    name = models.CharField(max_length=100, verbose_name='分类名')
    def __str__(self):
        return self.name
    class Meta:
        # 单数时显示的名称
        verbose_name = '分类'
        # 复数时显示的名称
        verbose_name_plural = '分类'

class Tag(models.Model):
    """标签表"""
    name = models.CharField(max_length=100, verbose_name='标签名')
    def __str__(self):
        return self.name
    class Meta:
        # 单数时显示的名称
        verbose_name = '标签'
        # 复数时显示的名称
        verbose_name_plural = '标签'


class Post(models.Model):
    """
   博客表
   """
    # 文章标题

    title = models.CharField(max_length=70, verbose_name='标题')
    # 文章正文,我们使用了 TextField。
    body = models.TextField(verbose_name='正文')
    # 这两个列分别表示文章的创建时间和最后一次修改时间,存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')
    modified_time = models.DateTimeField(default=datetime.now(), verbose_name='修改时间')
    # 文章摘要,可以没有文章摘要,但默认情况下 CharField 要求我们必须存入数据,否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。

    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    # 如果你对 ForeignKey、ManyToManyField 不了解,请看教程中的解释,亦可参考官方文档:
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category, verbose_name='分类',on_delete=False)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    # 文章作者,这里 User 是从 django.contrib.auth.models 导入的。
    # 因为我们规定一篇文章只能有一个作者,而一个作者可能会写多篇文章,因此这是一对多的关联关系,和 Category 类似。
    # author = models.ForeignKey(User, verbose_name='作者',on_delete=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    class Meta:
        # 单数时显示的名称
        verbose_name = '博客'
        # 复数时显示的名称
        verbose_name_plural = '博客'