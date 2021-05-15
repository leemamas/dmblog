# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/4/30  8:09
from django import template
from app import models
from django.db.models import Count

register=template.Library()

@register.inclusion_tag('right.html')
def getRight():
    tag_list=models.Tag.objects.annotate(c=Count('article__title')).all()
    category_list=models.Category.objects.annotate(c=Count('article__title')).all()
    return locals()

@register.inclusion_tag('title.html')
def getTitle():
    blog=models.Blog.objects.first()
    if not blog:
        blog = models.Blog.objects.create(title='呆马蓝的天空')

    return locals()

@register.inclusion_tag('site_name.html')
def getSiteName():
    blog=models.Blog.objects.first()
    if not blog:
        blog = models.Blog.objects.create(title='呆马蓝的天空')

    return locals()


@register.inclusion_tag('manage/title.html')
def getBgdoor():
    blog=models.Blog.objects.first()
    if not blog:
        blog = models.Blog.objects.create(title='呆马蓝的天空')

    return locals()