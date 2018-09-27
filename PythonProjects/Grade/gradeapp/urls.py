from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^stuname/$',views.stuname),
    url(r'^Login/$',views.Login),
    url(r'^Login/test2/$',views.test2),
    url(r'^t2/$',views.t2),
    url(r'^static1/$',views.static1),
    url(r'^fileup/$',views.fileup),
    url(r'^filesave/$',views.filesave),
]