from django.contrib import admin
from .models import *

# Custom admin interface for the Cart model
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

# Custom admin interface for the CartItem model
class CartItemAdmin(admin.ModelAdmin):
    list_display =('product', 'cart', 'quantity', 'is_active')

# Register your models here
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
