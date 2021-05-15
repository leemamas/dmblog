from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

##用户
class User(AbstractUser):
    nid = models.AutoField(primary_key=True)

    nickname=models.CharField(max_length=16,null=None,unique=True,default='呆马')
    position=models.CharField(max_length=16,null=None,unique=True,default='人类被研究对象')
    telphone=models.CharField(max_length=11,null=None,unique=True)
    avatar=models.FileField(upload_to='img/avatars/',default='img/avatars/default.png')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

##文章
class Article(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='文章标题', max_length=50)
    desc = models.CharField(verbose_name='描述', max_length=255)

    content = models.TextField()

    user = models.ForeignKey(verbose_name='作者', to='User', to_field='nid', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', to_field='nid', null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(to='Tag', through='Article2Tag', through_fields=('article', 'tag'))

    hot=models.BooleanField(default=True)

    create_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    modify_time = models.DateTimeField('修改时间', auto_now=True)

##分类
class Category(models.Model):

    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='分类标题',max_length=32)

##标签
class Tag(models.Model):

    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='标签名称',max_length=32)


class Article2Tag(models.Model):
    nid=models.AutoField(primary_key=True)

    article=models.ForeignKey(verbose_name='文章',to='Article',to_field='nid',on_delete=models.CASCADE)
    tag=models.ForeignKey(verbose_name='标签',to='Tag',to_field='nid',on_delete=models.CASCADE)

    class Meta:
        unique_together=[('article','tag'),]

class Contact(models.Model):

    nid = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name='留意者',max_length=32)
    content=models.CharField(verbose_name='留言内容',max_length=255)
    create_time=models.DateTimeField(verbose_name='留言时间',auto_now_add=True)
    parent_comment=models.ForeignKey('self',null=True,on_delete=models.CASCADE)

class Blog(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=64)
    site_name = models.CharField(verbose_name='站点名称', max_length=64,default='呆马蓝的天空')
    bgdoor_name = models.CharField(verbose_name='后台站点名称', max_length=64,default='呆马蓝的后花园')
    pic1 = models.FileField(upload_to='img/lunbo/', default='img/lunbo/default1.png')
    pic2 = models.FileField(upload_to='img/lunbo/', default='img/lunbo/default2.png')
    pic3 = models.FileField(upload_to='img/lunbo/', default='img/lunbo/default3.png')
    pic4 = models.FileField(upload_to='img/lunbo/', default='img/lunbo/default4.png')
    link = models.ForeignKey(to='Link', to_field='nid', null=True, on_delete=models.CASCADE)


class Link(models.Model):

    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='友链名称',max_length=32)
    url=models.CharField(verbose_name='友链地址',max_length=128)