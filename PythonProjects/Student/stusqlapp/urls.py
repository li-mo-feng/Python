from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^stulist/$',views.stulist),
    url(r'^test1/$',views.test1),
    url(r'^test2/',views.test2)
    # url(r"^statictest/$",views.static)
]