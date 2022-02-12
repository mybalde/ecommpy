from django.urls import path
from . import views

urlpatterns=[
    path('', views.cart, name='cart'),
    path('add_cart/<str:product_id>', views.add_cart, name='add_cart'),
    path('remove_cart/<str:product_id>', views.remove_cart, name='remove_cart'),
    path('remove/<str:product_id>', views.remove, name='remove'),
]