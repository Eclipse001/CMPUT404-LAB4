from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<question_id>[0-9a-z]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9a-z]+)/results/$',views.results,name='results'),
    url(r'^(?P<question_id>[0-9a-z]+)/vote/$',views.vote,name='vote'),
]