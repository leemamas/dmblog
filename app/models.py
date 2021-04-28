from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    nid = models.AutoField(primary_key=True)
    telphone=models.CharField(max_length=11,null=None,unique=True)
    avatar=models.FileField(upload_to='img/avatars/',default='img/avatars/default.png')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)

