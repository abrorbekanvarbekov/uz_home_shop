from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    email = models.EmailField(null=True,blank=True,help_text=u'user_email')
    product_image = models.ImageField(default="")
    management_code = models.CharField(max_length=10,blank=True,null=True,help_text=u'상품 관리용 코드')
    name = models.CharField(max_length=128, help_text=u'상품 이름')
    standard_price = models.IntegerField(default=0, null=True,blank=True,help_text=u'정가')
    original_sell_price = models.IntegerField(default=0,null=True, blank=True,help_text=u'기준 판매가')
    sell_price = models.IntegerField(null=True,blank=True,help_text=u'현재 판매가')
    original_cost = models.IntegerField(default=0,null=True,blank=True,help_text=u'기존 제조 원가/ 공급가액')
    pro_seil_prace = models.CharField(max_length=10,null=True,blank=True,help_text=u"세일 가격")
    pro_seil_percent = models.CharField(max_length=10,null=True,blank=True,help_text=u"세일 %")
    cost = models.IntegerField(default=0, blank=True,null=True, help_text=u"현재 제조 원가/공급가액")
    pro_manual = models.TextField(blank=True, null=True, help_text = u"상품 설명서")
    sales_count = models.IntegerField(default=0, blank=True,null=True, help_text=u"총 판매 수량")
    current_stock = models.IntegerField(default=0, blank=True,null=True, help_text=u"현재 재고 수준")
    safety_stock = models.IntegerField(default=0, blank=True,null=True,help_text=u"안전 재고 수준")

    created_time = models.DateTimeField(blank=True, null=True,auto_now_add=timezone.now())
    is_soldout = models.IntegerField(default=0, blank=True,null=True, help_text=u"재고 없음")

    class Meta:
        db_table="Product"


# class Category(models.Model):
#     name = models.CharField(max_length=32, help_text=u"category name")
#     index = models.IntegerField(default=0, null=True, help_text=u"category 표시 순서 적을수록 위 순위")
    
#     class Meta:
#         db_table="Category"


# class SubCategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=32, help_text=u"subcategory name")
#     index = models.IntegerField(default=0, null=True, help_text=u"subcategory 순서 적을수록 위 순위")

#     class Meta:
#         db_table="SubCategory"


# class ShopProduct(models.Model):
#     categorys = models.ManyToManyField(Category)
#     sub_categorys = models.ManyToManyField(SubCategory)

#     class Meta:
#         db_table="ShopProduct"
