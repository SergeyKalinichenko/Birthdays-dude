from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.greeting, name='greeting'),
    url(r'^polls/$', views.index_view, name='index'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.results_view, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/add_question/$', views.add_question, name='add_question'),
    url(r'^contact/$', views.contact, name='contact'),
    #url(r'^(?P<question_id>[0-9]+)/contact/$', views.contact, name='contact'),
]

