from django.db import models
from product.models import Product
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, help_text=u"category name")
    index = models.IntegerField(default=0, null=True, help_text=u"category 표시 순서 적을수록 위 순위")
    
    class Meta:
        db_table="Category"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, help_text=u"subcategory name")
    index = models.IntegerField(default=0, null=True, help_text=u"subcategory 순서 적을수록 위 순위")

    class Meta:
        db_table="SubCategory"


class ShopProduct(models.Model):
    categorys = models.ManyToManyField(Category)
    sub_categorys = models.ManyToManyField(SubCategory)

    class Meta:
        db_table="ShopProduct"

        
class Category_id(models.Model):
    cat_id = models.IntegerField()