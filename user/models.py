from this import d
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(unique=True,null=True,blank=True)
    nickname = models.CharField(unique=True,max_length=20,default=0,null=True,blank=True)
    name = models.CharField(max_length=30,unique=True,default="",null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100,default="",null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "name"
    
    class Meta:
        db_table = "User"
