import os

from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from app import forms,models
from blog import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def test(request):
    return HttpResponse('test')


def index(request):
    return render(request,'index.html',locals())


def login(request):

    if not request.user.is_authenticated:
        if request.method=='POST':
            username = request.POST.get('user')
            password = request.POST.get('pwd')

            user=auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return redirect('/manage/')

        return render(request, 'manage/login.html', locals())

    return redirect('/manage/')



def logout(request):
    auth.logout(request)
    return redirect('/login/')



@login_required(login_url='/login/')
def manage(request):
    return render(request,'manage/index.html',locals())


@login_required()
def userinfo(request):
    return render(request,'manage/userinfo.html',locals())

@login_required()
def user(request):
    ret={}

    if request.is_ajax():
        userForm = forms.UserForm(request.POST)
        # username=request.POST.get('username')
        # telphone=request.POST.get('telphone')
        # email=request.POST.get('email')
        # avatar=request.FILES.get('avatar')

        if userForm.is_valid():

            username=userForm.cleaned_data.get('username')

            # extra = {}
            # if avatar_obj:
            #     extra['avatar'] = avatar_obj
            #models.User.objects.filter(username=username).update(**userForm.cleaned_data,**extra)
            ##更新数据
            models.User.objects.filter(username=username).update(**userForm.cleaned_data)

            avatar_obj = request.FILES.get('avatar')
            if avatar_obj:
                user_obj = models.User.objects.filter(username=username).first()
                user_obj.avatar=avatar_obj
                user_obj.save()

            ret['status'] = 0
        else:
            ##错误信息
            errors=userForm.errors.get_json_data()
            error={}
            for key, message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                error[key] = messages

            ret['status'] = 1
            ret['error'] = error

    return JsonResponse(ret)


@login_required()
def article(request):
    return render(request,'manage/article.html',locals())


#############################【标签】#####################################
@login_required()
def tag(request):
    list = models.Tag.objects.all()
    return render(request,'manage/tag.html',locals())

@login_required()
@csrf_exempt
def add_tag(request):
    ret={}
    form = forms.TagForm(request.POST)
    if form.is_valid():
        models.Tag.objects.create(**form.cleaned_data)
        ret['status']=0
    else:

        error=form.getError()

        ret['status'] = 1
        ret['error'] = error
    return JsonResponse(ret)

@login_required()
@csrf_exempt
def edit_tag(request,id):
    ret={}
    form = forms.TagForm(request.POST)
    if form.is_valid():
        models.Tag.objects.filter(nid=id).update(**form.cleaned_data)
        ret['status'] = 0
    else:

        error=form.getError()
        ret['status'] = 1
        ret['error'] = error

    return JsonResponse(ret)

@login_required()
@csrf_exempt
def del_tag(request,id):
    ret={}
    models.Tag.objects.filter(pk=id).delete()
    ret['status']=0
    return JsonResponse(ret)



##############################【分类】############################################
@login_required()
def category(request):
    list = models.Category.objects.all()
    return render(request,'manage/category.html',locals())

@login_required()
@csrf_exempt
def add_category(request):
    ret={}
    form = forms.CategoryForm(request.POST)
    if form.is_valid():
        models.Category.objects.create(**form.cleaned_data)
        ret['status']=0
    else:

        error=form.getError()

        ret['status'] = 1
        ret['error'] = error
    return JsonResponse(ret)

@login_required()
@csrf_exempt
def edit_category(request,id):
    ret={}
    form = forms.CategoryForm(request.POST)
    if form.is_valid():
        models.Category.objects.filter(nid=id).update(**form.cleaned_data)
        ret['status'] = 0
    else:

        error=form.getError()
        ret['status'] = 1
        ret['error'] = error

    return JsonResponse(ret)

@login_required()
@csrf_exempt
def del_category(request,id):
    ret={}
    models.Category.objects.filter(pk=id).delete()
    ret['status']=0
    return JsonResponse(ret)


def upload(request):

    print(request.FILES)
    img=request.FILES.get('upload_img')
    path=os.path.join(settings.MEDIA_ROOT,'article_img',img.name)
    #TODO 没创建文件夹会出错
    with open(path,'wb') as f:
        for line in img:
            f.write(line)
    result={
        'error':0,
        'url':'/media/article_img/%s'%img.name
    }

    return JsonResponse(result)


def blog(request):
    return render(request,'blog.html',locals())

def about(request):
    return render(request,'about.html',locals())

def contact(request):
    return render(request,'contact.html',locals())

def single(request):
    return render(request,'single.html',locals())