from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError
# Create your views here.

@csrf_exempt
def Id_Check(request):
    nickname = request.GET.get('nickname')
    nickname_list = User.objects.values_list("nickname",flat=True)
    if nickname in nickname_list:
        overlap = "fail"
    else:
        overlap = "pass"
    context = {'overlap':overlap}
    return JsonResponse(context)


@csrf_exempt
def Email_check(request):
    email = request.GET.get('email')
    email_list = User.objects.values_list('email',flat=True)
    if email in email_list:
            overlap = "fail"
    else:
            overlap = "pass"
    if not '@' in email or not '.' in email:
            overlap = "fail1"

    context = {'overlap':overlap}
    return JsonResponse(context)


class Join(APIView):
    @csrf_exempt
    def get(self, request):
        email = request.session.get('email',None)
        user = User.objects.filter(email=email).first()
        return render (request, "user/join.html", context=dict(user=user))
          
                
    @csrf_exempt
    def post(self, request):
        nickname= request.data.get('nickname',None)
        email = request.data.get("email",None)
        password = request.data.get("password",None)
        name = request.data.get("name",None)
        phone_number = request.data.get("phone_number",None)
        address = request.data.get('address',None)
        print(address)
        # home_address = request.data.get('home_address',None)
        User.objects.create(
                    nickname=nickname,
                    email=email,
                    password=make_password(password),
                    name=name,
                    phone_number=phone_number,
                    address=address,
                    # home_address=home_address
                    )
        # return Response(status=200)
        return Response(data={'detail':['You can use this ID']}, status=200)



class Login(APIView):
    @csrf_exempt
    def get(self, request):
        email = request.session.get('email',None)
        user = User.objects.filter(email=email).first()
        return render(request, "user/login.html", context=dict(user=user))

    @csrf_exempt
    def post(self, request):
        email_id = request.data.get("email",None)
        password = request.data.get("password",None)
        user = User.objects.filter(email=email_id).first()
        if user is None:
            user1 = User.objects.filter(nickname=email_id).first()
            if user1 is None:
                return Response(status=404,)
            else:
                return Response(status=200)
            # return Response(status=404,)
        # if User.objects.all().filter(email=email,password=password).exists()==True:
        if user.check_password(password):
            # TODO 로그인을 했다. 세션 or 쿠키
            request.session['email'] = email_id
            request.session['user_id']=user.id
            return Response(status=200)
        else:
            user.check_password(password)
            # TODO 로그인을 했다. 세션 or 쿠키
            request.session['email'] = email_id
            request.session['user_id']=user.id
            return Response(status=200)



class LogOut(APIView):
    @csrf_exempt
    def get(self,request):
        request.session.flush()
        return render(request, 'user/login.html')


class MyProfile(APIView):
    @csrf_exempt
    def get(self, request):
        email = request.session.get('email',None)
        user = User.objects.filter(email = email)
        return render(request, 'user/my_profile.html',context=dict(user=user))


class Find_Id(APIView):
    def get(self, request):
        
        return render(request, "user/find_id.html")

    def post(self, request):
        type = request.data.get('type',None)
        name = request.data.get('name',None)
        phone_email = request.data.get(f'{type}',None)
        if type == "phone":
            user = User.objects.filter(name=name,phone_number=phone_email)
        elif type == "email":
            user = User.objects.filter(name=name,email=phone_email)

        if user:
            print(user)
        else:
            return Response(status=404)
        return render(request, "user/find_id.html")


class Find_Pw(APIView):
    def get(self, request):
        
        return render(request, "user/find_pw.html")

    def post(self, request):
        type = request.data.get('type',None)
        name = request.data.get('name',None)
        phone_email = request.data.get(f'{type}',None)
        if type == "phone":
            user = User.objects.filter(name=name,phone_number=phone_email)
        elif type == "email":
            user = User.objects.filter(name=name,email=phone_email)
            
        if user:
            print(user.name)
        else:
            print('error')
        return render(request, "user/find_pw.html")


























# class SuperUser_Login(APIView):
#     def get(self, request):
#         return render(request, 'user/superuser_login.html')

#     def post(self, request):
#         email = request.data.get('email',None)
#         password = request.data.get('password',None)

#         user = User.objects.filter(email=email).first()

        
#         if user.is_admin ==True:
                
#             if user is None:
#                 return Response(status=404,)

#             if user.check_password(password):
#                 # TODO 로그인을 했다. 세션 or 쿠키
#                 request.session['email'] = email
#                 return Response(status=200)
                
#             else:
#                 return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))
#         else:
#             return Response(status=403)


# class SuperUserLogOut(APIView):
#     def get(self,request):
#         request.session.flush()
#         return render(request, 'user/login.html')