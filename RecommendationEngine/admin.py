from django.contrib import admin
from models import Product, ProductAttribute, ProductCategory


# Register your models here.

class ProductAdmin( admin.ModelAdmin ):
    pass


admin.site.register( Product, ProductAdmin )


class ProductAttributeAdmin( admin.ModelAdmin ):
    pass


admin.site.register( ProductAttribute, ProductAttributeAdmin )


class ProductCategoryAdmin( admin.ModelAdmin ):
    pass


admin.site.register(ProductCategory, ProductCategoryAdmin)
