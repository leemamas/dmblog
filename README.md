## 主要功能：
#### 前端
* 首页推荐文章显示、轮播图、右侧关于作者和友情链接
* 文章、分类、标签的展示
* 留言板功能
#### 后端
* 博客标题、站点、轮播图信息修改
* 个人信息的修改
* 文章,分类目录,标签的curd操作
* 留言查看与删除
* 友情链接相关操作

## 配置
* 修改数据库配置,在blog/settings.py下，根据自己需要选择
```python
##mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 数据库引擎
        'NAME': 'boke', # 数据库名
        'USER': 'root', # 账号
        'PASSWORD': 'toor', # 密码
        'HOST': '127.0.0.1', # HOST
        'POST': 3306, # 端口

    }
}
##sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
* 迁移数据
```shell script
./manage.py makemigrations
./manage.py migrate
```
* 创建超级用户
```shell script
./manage.py createsuperuser
```
## 运行

```shell script
./manage.py runserver
```
浏览器打开: http://127.0.0.1:8000/ 就可以看到效果了

## 问题相关
有任何问题欢迎提Issue,或者将问题描述发送至我邮箱76854100#163.com.我会尽快解答.推荐提交Issue方式.