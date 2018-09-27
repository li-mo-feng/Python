from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator
import os
# Create your views here.
# -------------纯跳转--------------
def index(request):
    return render(request,"index.html")
# 主页
def login(request):
    return render(request,"login.html")
# 登陆页面跳转
def user_sadmin(request):
    return  render(request,"sadmin_login.html")
# 狗管理登陆
def user_zhigong(request):
    return  render(request,"zhigong_login.html")
# 职工登陆
def user_yezhu(request):
    return  render(request,"yezhu_login.html")
# 业主登陆
def top(request):
    return render(request,"top.html")
# 后台页面框架顶层
def left(request):
    return render(request,"left.html")
# 后台页面框架左侧菜单栏
def right(request):
    return render(request,"right.html")
# 后台页面框架主要显示区
def footer(request):
    return render(request,"footer.html")
# 后台页面底部框架显示区
def regist(request):
    return render(request,"regist.html")
# 注册页面

# ------------纯跳转-----------------------

# -------------功能------------------------
# =============
# =============登陆模块=====================
def user_login(request):
    # 登陆页面获取的数据处理跳转
    inuser=user()
    inuser.user_id=request.POST.get("userid")
    request.session['userid']=inuser.user_id
    y=request.session.get('userid')
    # 获取用户id
    print(inuser.user_id)
    # 测试w
    inuser.user_password=request.POST.get("userpassword")
    # 获取用户密码
    print(inuser.user_password)
    # 测试
    inuser.user_type=request.POST.get("type")
    # 获取用户类型
    print(inuser.user_type)
    # 测试
    inuserinfor=user.objects.filter(user_id=inuser.user_id,
                                    user_password=inuser.user_password,
                                    user_type=inuser.user_type)
    # 首先判断数据是否存在
    if inuserinfor:
        request.session['getid'] = inuser.user_id
        if inuser.user_type=="sadmin":
            return render(request, "user_login.html", {"inuserinfor": 1})
        elif inuser.user_type=="yezhu":
            # 判断是否是业主
            # return HttpResponse("业主")
            return render(request, "user_login.html",{"inuserinfor":2,})
        elif inuser.user_type == "zhigong":
            # 或许是职工
            # return HttpResponse("职工")
            return render(request, "user_login.html",{"inuserinfor":3,})
    else:
        # 帐号或者密码错误
        return render(request, "user_login.html", {"inuserinfor": 0, })
        return HttpResponseRedirect("index")

    # --------------------------------登陆模块----------------------------
# =============注册模块-====================
def regist_check(request):
    bdata =building.objects.all()
    rdata =room.objects.all()
    udata =user.objects.all()
    # 三大数据表对象
    name=request.POST.get("uname")
    upassword=request.POST.get("upaswrod")
    uphonenum=request.POST.get("uphonenum")
    ucardnum=request.POST.get("ucardnum")
    uroomum=request.POST.get("uroomum")
    # 接受ajax传过来的值！

    # 下部分是判断用户名是否存在的判断
    for bu in udata:
        # print(bu.user_name)
        if name==upassword==uphonenum==ucardnum==uroomum==None:
            print(name)
            print(upassword)
            print(uphonenum)
            print(ucardnum)
            print(uroomum)
            pass
        else:
            if name==bu.user_name:
                # 输入用户名和数据库内数据的相同判断
                return JsonResponse({"res": 0})
            # 因为考虑到同名同姓的情况故判断舍弃。用身份证号码做唯一判断
            elif ucardnum==bu.user_cardnum:
                # 身份证
                return JsonResponse({"res":1})
            elif uphonenum==bu.user_phonenum:
                # 手机号码
                return JsonResponse({"res":2})


def uregist(request):
    user.user_roomid=room()
    newre = user()
    # uid=newre.user_id=request.POST.get("uid")
    newre.user_name=request.POST.get("uname")

    # print(newre.user_name)
    newre.user_id=request.POST.get("ucardnum")
    newre.user_password = request.POST.get("upassword")
    newre.user_phonenum = request.POST.get("uphonenum")
    # print(newre.user_phonenum)
    newre.user_cardnum = request.POST.get("ucardnum")
    newre.user_roomid=request.POST.get("uroomid")
    newre.user_type = request.POST.get("type")
    newre.user_sex = request.POST.get("sex")
    newre.save()
    return render(request,"uregist.html")
# ==============楼栋数据修改=================

# 1.删除大楼数据-----------------------------
def budelete(request):
    data=building.objects.all()
    return render(request,"budelete.html",{"data":data})
# 2.修改
def buupdate(request):
    data = building.objects.all()
    return render(request,"buupdate.html",{"data":data})

def bu_update(request):
    # 获得各项数据
    # 楼栋名称，楼栋动工时间，楼栋完工时间，楼栋层数，楼栋施工方，楼栋监理方

    gtname=request.POST.get("buname")
    # print(gtname)
    gtsdate=request.POST.get("busdate")
    print(gtsdate)
    gtedate=request.POST.get("buedate")
    print(gtedate)
    gtfloor=request.POST.get("bufloor")
    # print(gtfloor)
    gtbcp = request.POST.get("bubcp")
    # print(gtbcp)
    gtsvcp = request.POST.get("busvcp")


    building.objects.filter(building_name=gtname).update(building_sdate=gtsdate,building_floor=gtfloor
                                                         ,building_edate=gtedate,building_bcp=gtbcp
                                                         ,building_svcp=gtsvcp)
    return render(request,"bu_update.html")

# =3.新增大楼===============================
def bunewbuilding(request):
    data =building.objects.all()
    return render(request,"bunewbuilding.html",{"data":data})


def bu_new(request):
        nbu=building()
        nbu.building_name=request.POST.get("buname")
        nbu.building_sdate=request.POST.get("busdate")
        nbu.building_edate=request.POST.get("buedate")
        nbu.building_floor=request.POST.get("bufloor")
        nbu.building_bcp=request.POST.get("bubcp")
        nbu.building_svcp=request.POST.get("busvcp")
        nbu.save()
        return render(request,"bu_new.html")




# ==4.查询大楼==============================
def busearch(request):
    data =building.objects.all()
    return render(request,"busearch.html",{"data":data})

# =========================================

# ============房间数据=======================

# 1.删除房间数据------------------------------
def rodelete(request):
    data=room.objects.all()
    return render(request,"rodelete.html",{"data":data})
    # =========================
# 2.删除操作
    indexs=request.POST.get('indexs')
    print(indexs)
    building.objects.filter(building_name=indexs).delete()
# 2.修改房间数据
def roupdate(request):
        bdata =building.objects.all()
        rdata =room.objects.all()
        udata =user.objects.all()
        return render(request,"roupdate.html",{"rdata":rdata,"bdata":bdata,"udata":udata})
# =3.新增房间===========================
def ronewroom(request):
    # 将三张表的数据对象传递到页面上
    bdata =building.objects.all()
    rdata =room.objects.all()
    udata =user.objects.all()
    return render(request,"ronewroom.html",{"rdata":rdata,"bdata":bdata,"udata":udata})


# ==4.查询房间信息=============================
def rosearch(request):
    data =room.objects.all()
    return render(request,"rosearch.html",{"data":data})
# ===============END=========================


# ===================人员管理==================
# =========人员查询
def psearch(request):
    bdata =building.objects.all()
    rdata =room.objects.all()
    udata =user.objects.all()
    return render(request,"psearch.html",{"rdata":rdata,"bdata":bdata,"udata":udata})

# ==========人员删除==========================
def pdelete(request):
    bdata =building.objects.all()
    rdata =room.objects.all()
    udata =user.objects.all()
    return render(request,"pdelete.html",{"rdata":rdata,"bdata":bdata,"udata":udata})
# =========人员信息修改
def pupdate(request):
    bdata =building.objects.all()
    rdata =room.objects.all()
    udata =user.objects.all()
    return render(request,"pupdate.html",{"rdata":rdata,"bdata":bdata,"udata":udata})
# ===========人员新增
def pnewperson(request):
    bdata = building.objects.all()
    rdata = room.objects.all()
    udata = user.objects.all()
    return render(request, "pnewperson.html", {"rdata": rdata, "bdata": bdata, "udata": udata})











































