from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from product.models import Product
from main.models import Category, Category_id
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
# @csrf_exempt

class Main(APIView):
    @csrf_exempt
    def get(self, request):
        product_object_list=Product.objects.all().order_by('-id')
        product_list=[]
        for product in product_object_list:
            product_list.append(dict(
                id = product.id,
                product_image = product.product_image,
                name= product.name,
                pro_seil_prace=product.pro_seil_prace,
                pro_seil_percent=product.pro_seil_percent,
                sell_price=product.sell_price,    
            ))
        email = request.session.get('email',None)

        user = User.objects.filter(email=email).first()
       
        return render(request, 'main/main.html',context=dict(
                                                products=product_list,
                                                user=user,
                                                ))


@csrf_exempt
def Search_fun(request):
        search_keyword = request.GET['q']
        search_product_list = Product.objects.filter(Q(name__icontains=search_keyword))
        context = {
            'search_keyword':search_keyword,
            'search_product_list':search_product_list
        }
        return render(request, 'main/search.html',context)
   


def Read_more(request,id):
    products = Product.objects.filter(id=id)
    email = request.session.get('email',None)
    user = User.objects.filter(email=email).first()
    return render(request, 'main/read_more.html', context=dict(products=products, user=user))


class New_product(APIView):
    @csrf_exempt
    def get(self, request):
        product_list = Product.objects.filter().order_by('-created_time')
        return render(request, 'main/new_product.html', context=dict(product_list=product_list))



class Best(APIView):
    def get(self, request):
        return render(request, 'main/best.html')


class Thrifty_shopping(APIView):
    @csrf_exempt
    def get(self, request):
        return render(request, 'main/thrifty_shopping.html')


