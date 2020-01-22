from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('', views.login_user, name='index'),
    path('tpinformation/', views.info_tp, name='infotp'),
    path('tp_filter/', views.tp_filter, name='tp_filter'),
    path('list_filter/', views.list_filter, name='list_filter'),
    path('tcs_list/', views.tcs_list, name='tcs_list')



]
