"""
Date: 2019--22 14:58
User: yz
Email: 1147570523@qq.com
Desc:

"""
from django import template

from ..models import Post, Category, Tag

# 创建模板库对象
register = template.Library()


# 将函数 get_recent_posts添加到模板中
@register.simple_tag
def get_recent_posts(num=3):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
   # 别忘了在顶部引入 Category 类
   return Category.objects.all()

@register.simple_tag
def get_tags():
    # 标签类
    return Tag.objects.all()

