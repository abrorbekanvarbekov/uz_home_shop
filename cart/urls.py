from django.urls import path
from .views import add_cart, cart_delite, cart_detail,quantity_minus,quantity_plus,cart_delite

app_name = "cart"

urlpatterns = [
    path('add/<int:product_id>/', add_cart, name='add_cart'),
    path('', cart_detail, name='cart_detail'),
    path('plus/',quantity_plus, name='quantity_plus'),
    path('minus/', quantity_minus, name='quantity_minus'),
    path('delite/<int:id>', cart_delite, name="cart_delite")
    
]