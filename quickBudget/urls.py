from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'quickBudget'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^budget$', views.budget, name='budget'),
    url(r'^submit$', views.submit, name='submit'),
]
