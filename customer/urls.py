from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('register_customers',views.register_customers, name='register_customers'),
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('after_login',views.after_login, name='after_login'),
    path('purchase/<int:idd>',views.purchase, name='purchase'),





]