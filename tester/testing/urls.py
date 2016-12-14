from django.conf.urls import url
from .views import IndexView, RedirectToQuestions, QuestionDetail

app_name = 'tester'
urlpatterns=[
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', RedirectToQuestions.as_view(), name='redirect_to_questions'),
    url(r'^(?P<test_pk>[0-9]+)/(?P<question_num>[0-9]+)/$', QuestionDetail.as_view(), name='question'),

    url(r'^vote$', QuestionDetail.as_view(), name='vote'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]