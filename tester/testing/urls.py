from django.conf.urls import url
from . import views

app_name = 'tester'
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<title_id>[0-9]+)/$', views.test, name='test'),
    url(r'^(?P<title_id>[0-9]+)/vote$', views.vote, name='vote'),

    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]