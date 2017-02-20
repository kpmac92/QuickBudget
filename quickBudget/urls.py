from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'quickBudget'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /budget/5/
    #url(r'^(?P<budget_id>[0-9]+)/$', views.budget, name='budget'),
    url(r'^budget$', views.budget, name='budget'),
]
