from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^show/(?P<id>\d+)$', views.show, name = 'my_show'),
    url(r'^new/$', views.new, name = 'my_new'),
    url(r'^create/$', views.create, name = 'my_create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name = 'my_edit'),
    url(r'^update/(?P<id>\d+)$', views.update, name = 'my_update'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = 'my_destroy'),
]
