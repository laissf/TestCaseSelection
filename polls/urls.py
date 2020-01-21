from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('tpinformation/', views.info_tp, name='infotp'), #name - info que vai no html também
    path('filter/', views.tp_filter, name='filter'),
    path('list_filter/', views.list_filter, name='list_filter'),



]
