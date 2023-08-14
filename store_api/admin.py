from django.contrib import admin
from .models import Product, Category


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