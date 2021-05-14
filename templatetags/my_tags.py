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