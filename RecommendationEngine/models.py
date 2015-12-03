from django.db import models
import datetime
# Create your models here.


class ProductAttribute(models.Model):
    product_attribute_id =models.AutoField(primary_key=True)
    attribute_brand = models.CharField(max_length=50)
    attribute_inventory = models.IntegerField()
    attribute_shipping_condition = models.BooleanField()
    attribute_description = models.TextField()
    attribute_target_url = models.CharField(max_length=255 , blank=False)

    def __str__(self):
        return self.product_attribute_id

class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    category_code = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    category_parent = models.ForeignKey('self' , blank=True , null=True , related_name='child')

    def __str__(self):
        return self.product_category_id


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    product_code = models.CharField(max_length=500)
    product_attribute = models.ForeignKey(ProductAttribute,related_name="attributes")
    product_category = models.ManyToManyField(ProductCategory, blank=True, verbose_name=("Category"))
    product_date_added = models.DateField(null=True  , blank=True)

    def __str__(self):
        return self.product_code

    @property
    def _get_MainCategory(self):
        """Return the first category for interested product"""
        if self.product_category.count() > 0 :
            return self.product_category.all()[0]
        else :
            return None











