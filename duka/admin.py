from django.contrib import admin
from .models import Product, ShoppingCart, ShoppingCartItem
# Register your models here.

admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)
