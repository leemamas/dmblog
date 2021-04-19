from django.shortcuts import render,HttpResponse

# Create your views here.
def test(request):
    return HttpResponse('test')


def index(request):
    return render(request,'index.html',locals())


def login(request):
    error=''
    if request.method=='POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user=='aaa' and pwd=='aaa':
            return render(request,'manage/index.html',locals())
        else:
            return render(request, '404.html', locals())

    return render(request, 'manage/login.html', locals())


def manage(request):
    return render(request,'manage/index.html',locals())
