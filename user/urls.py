from django.urls import path
from .views import *

urlpatterns = [
    path('join/',Join.as_view(),name='join'),
    path('login/',Login.as_view(),name='user_login'),
    path('logout/',LogOut.as_view(), name ='user_logout' ),
    path('myprofile',MyProfile.as_view(),name='my_profile'),
    path('join_id_check/',Id_Check, name='Id_check'),
    path('join_email_check/',Email_check, name="Email_check"),
    path('find_id/',Find_Id.as_view(),name="find_id"),
    path('find_pw/',Find_Pw.as_view(),name="find_pw")
    # path('superuser_login/',SuperUser_Login.as_view(),name="superuser_login"),
    # path('seperuserlogout/',SuperUserLogOut.as_view(), name='user_logout')
]