# from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    path("", views.post_list, name="post_list"),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
]