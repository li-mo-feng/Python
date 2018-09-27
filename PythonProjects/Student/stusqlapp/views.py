from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("hhhh")

from .models import stu_infor,grade

def stulist(request):
    sl=stu_infor.objects.all().stu_name
    return render(request,'/stusqlapp/stulist.html',{'sl':sl})

def test1(request):
    return render(request,'stusqlapp/test1.html')
def test2(request):
    return HttpResponse('hhhh')

