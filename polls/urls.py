from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('tpinformation/', views.info_tp, name='infotp'), #name - info que vai no html também
    path('filter/', views.list_filters, name='filter'),




]
