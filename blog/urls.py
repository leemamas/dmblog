
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve
from blog import settings
from app import views
from django.conf.urls import handler404, handler500

handler404=views.page_not_found
handler500=views.page_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',views.test),
    path('',views.index,name='home'),

    path('about/',views.about),
    path('contact/',views.contact),

    path('login/',views.login),
    path('logout/',views.logout,name='logout'),
    path('user/',views.user),
    path('manage/',views.manage),
    path('manage/userinfo/',views.userinfo),

    path('article/',views.article),
    path('article/<id>/',views.articleinfo),

    path('tag/',views.tag),
    path('tag/<id>/',views.taginfo),


    path('category/',views.category),
    path('category/<id>/',views.categoryinfo),



    path('manage/article/',views.list_article),
    path('manage/ajaxGetArticle/<id>/',views.ajaxGetArticle),
    path('manage/add_article/',views.add_article),
    path('manage/edit_article/<id>/', views.edit_article),
    path('manage/del_article/<id>/', views.del_article),

    path('manage/tag/',views.list_tag),
    path('manage/add_tag/', views.add_tag),
    path('manage/edit_tag/<id>/', views.edit_tag),
    path('manage/del_tag/<id>/', views.del_tag),

    path('manage/category/',views.list_category),
    path('manage/add_category/',views.add_category),
    path('manage/edit_category/<id>/',views.edit_category),
    path('manage/del_category/<id>/',views.del_category),

    re_path(r"media/(?P<path>.*)$",serve,{"document_root":settings.MEDIA_ROOT}),
    path('upload/',views.upload ),

]
