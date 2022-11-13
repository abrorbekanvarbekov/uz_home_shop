from django.urls import path
from .views import Product_add 
urlpatterns= [
    path('product_add/', Product_add.as_view(),name="product_add"),
    # path('cart_add/<int:id>/', Cart_add, name="cart_add"),
]