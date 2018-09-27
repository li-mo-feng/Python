from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^index/top.html$',views.top),
    url(r'^index/left.html$',views.left),
    url(r'^index/right.html$',views.right),
    url(r'^index/footer.html$',views.footer),
    # ====================楼栋
    url(r'^index/buupdate.html$',views.buupdate),
    url(r'^index/bunewbuilding.html$',views.bunewbuilding),
    url(r'^index/busearch.html$',views.busearch),
    url(r'^index/budelete.html$',views.budelete),
    url(r'^bu_update/$',views.bu_update),
    url(r'^bu_new/$',views.bu_new),
    # ====================房间
    url(r'index/roupdate.html$', views.roupdate),
    url(r'index/ronewroom.html$', views.ronewroom),
    url(r'index/rosearch.html$', views.rosearch),
    url(r'index/rodelete.html$', views.rodelete),
    # ====================业主
    url(r'index/psearch.html$',views.psearch),
    url(r'index/pupdate.html$',views.pupdate),
    url(r'index/pnewperson.html$',views.pnewperson),
    url(r'index/pdelete.html$',views.pdelete),
    # ====================================
    url(r'^index/login.html$',views.login),
    url(r'^index/regist.html$',views.regist),
    url(r'^regist_check.html',views.regist_check),
    url(r'^index/uregist$',views.uregist),
    url(r'^index/user_login$',views.user_login),
    url(r'^index/sadmin.html$',views.user_sadmin),
    url(r'^index/zhigong.html$',views.user_zhigong),
    url(r'^index/yezhu.html$',views.user_yezhu),
]