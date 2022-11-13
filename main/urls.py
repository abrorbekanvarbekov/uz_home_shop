from django.urls import path
from .views import *


urlpatterns = [
    path('',Main.as_view(),name='main'),
    # path('<int:id>', Category_View.as_view(), name="category"),
    path('newproduct/', New_product.as_view(),name='new_product'),
    path('best/',Best.as_view(),name='best'),
    path('thriftyshopping/',Thrifty_shopping.as_view(),name='thrifty_shopping'),
    path('product/<int:id>/', Read_more, name='product'),
    path('search/', Search_fun, name='search')
    # path('prod_click/', Prod_click.as_view(), name="prod_click"),
    # path('category_id/', Cat_id.as_view(), name='category_id'),
]   