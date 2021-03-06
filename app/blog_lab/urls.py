from django.conf.urls import patterns, url

from app.blog_lab.proxy.views import create_permission, get_ip
from app.blog_lab.chart.views import get_chart_message
from app.blog_lab.views import *
from app.blog_lab.cbv.views import ArticleDetailView


urlpatterns = patterns('',
    url(r'^create_token/$', create_permission),
    url(r'^get_proxy/$', get_ip),
    url(r'^proxy/$', proxy),
    url(r'^monitor/$', monitor),
    url(r'^get_lab_info/$', get_lab_info),
    url(r'^get_chart_info/$', get_chart_message),
    url(r'^get_test_cbv/$', ArticleDetailView.as_view()),
    )