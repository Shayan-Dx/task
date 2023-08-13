from django.contrib import admin
from .models import Product, Category, User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_enable", "created_time"]
    list_filter = ["is_enable"]
    search_fields = ["title"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_enable", "created_time"]
    list_filter = ["is_enable"]
    search_fields = ["title"]
    filter_horizontal = ['categories']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "password", "name", "is_active", "is_staff"]
    list_filter = ["is_active"]
    search_fields = ["name"]