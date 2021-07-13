from django.urls import path

from . import views

app_name = 'lists'

urlpatterns = [
    path('', views.list_list, name='list_list'),
    path('new', views.list_create, name='list_new'),
]