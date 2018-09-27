from django.shortcuts import render
from django.http import HttpResponse
from .models import student,grade
from django.conf import settings
import os

# Create your views here.
def index(request):
    return HttpResponse('hhhh')


def stulist(request):
    return render(request,"stulist.html")

def stuname(request):
    stuname=student.objects.all()
    return  render(request,"stuname.html",{'stuname':stuname})
# rander有三个参数，第一个是request，第二个是传递的页面，第三个是传递的值


def Login(request):
    return render(request,'Login.html')

def test2(request):
    post=request.POST
    username=post.get("username")
    password=post.get("password")
    return render(request,'test2.html',{"username":username,"password":password})


def t2(request):
    return render(request,'t2.html')

def static1(request):
    return  render(request,'static1.html')

def fileup(request):
    return  render(request,'fileup.html')



#重点注意对象名的书写和pycharm的拼写检查


def filesave(request):
    # 首先获得文件
    fa=request.FILES.get("fa")
    # 然后是存储路径（）
    fspath=os.path.join(settings.BASE_DIR,"static/fileup")

    # 创建上传文件需要写入的目标文件,且文件名需要组合
    ufa=open(os.path.join(fspath,fa.name),"wb")
    for data in fa.chunks():
        ufa.write(data)
    ufa.close()
    return HttpResponse("上传成功")