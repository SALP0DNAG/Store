from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('basket-add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket-delete/<int:basket_id>/', views.basket_delete, name='basket_delete'),
]
