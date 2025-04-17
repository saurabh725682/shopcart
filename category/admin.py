from django.contrib import admin
from .models import *

# Custom admin interface for the Category model
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
