from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from product.models import Product
from rest_framework.response import Response
from uuid import uuid4
from config.settings import MEDIA_ROOT
import os
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class Product_add(APIView):
    @csrf_exempt
    def get(self, request):

        email = request.session.get('email',None)
        if email is None:
            return render(request, 'user/login.html')
        
        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, 'user/login.html')

        return render(request,"main/product_add.html")

    @csrf_exempt
    def post(self ,request):
        email = request.session.get('email',None)
        # management_code = request.data.get('management_code',None)
        name = request.data.get('name',None)
        # standard_price = request.data.get('standard_price',None)
        # original_sell_price = request.data.get('original_sell_price',None)
        sell_price = request.data.get('sell_price',None)
        # original_cost = request.data.get('original_cost',None)
        pro_seil_prace = request.data.get('pro_seil_prace',None)
        pro_seil_percent = request.data.get('pro_seil_percent',None)
        file = request.FILES["file"]
        uuid_name = uuid4().hex   # 이미지 이름 랜덤 정의
        save_path = os.path.join(MEDIA_ROOT,uuid_name)
        with open(save_path,'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        product_image = uuid_name
        Product.objects.create(
            email=email,
            product_image=product_image,
            # management_code=management_code,
            name=name,
            # standard_price=standard_price,
            # original_sell_price=original_sell_price,
            sell_price=sell_price,
            # original_cost=original_cost,
            pro_seil_percent=pro_seil_percent,
            pro_seil_prace=pro_seil_prace
        )
        return Response(status=200)


