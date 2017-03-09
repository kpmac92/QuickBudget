from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'quickBudget'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createBudget$', views.create_budget, name='createBudget'),
    url(r'^submit$', views.submit, name='submit'),
]
