from django.conf.urls import url

from . import views

app_name = 'myadmin'

urlpatterns = [
    url(r'^$', views.main, name='index'),
    url(r'^edit/(?P<id>[0-9]+)$', views.edit, name='edit'),
]
