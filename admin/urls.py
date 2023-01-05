from django.urls import path
from . import views

app_name = 'admin'
urlpatterns = [
    path('add_admin',views.add_admin, name='add_admin'),
    path('add_products',views.add_products, name='add_products'),
    path('index_admin',views.index_admin, name='index_admin'),
    path('view_products',views.view_products, name='view_products'),
    path('view_register',views.view_register, name='view_register'),
    path('view_purchase',views.view_purchase, name='view_purchase'),


    




]