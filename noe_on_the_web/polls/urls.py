from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^test/', views.test, name='test'),
    url(r'^(?P<question_id>[0-9]+)/*$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/*$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/*$', views.vote, name='vote'),
    url(r'^$', views.index, name='index'),
    url(r'.*', views.not_found, name='404'),
]
