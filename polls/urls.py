from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.login, name='index'),
    path('info_tp/', views.info_tp, name='info_tp'),
    path('tp_filter/', views.tp_filter, name='tp_filter'),
    path('list_filter/', views.list_filter, name='list_filter'),
    path('tcs_list/', views.tcs_list, name='tcs_list'),
    path('ajax/tcs_list/', views.ajax_tc_list, name='ajax_tcs_list'),



]
