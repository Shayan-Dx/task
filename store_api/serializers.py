from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, _ = Category.objects.get_or_create(**category_data) # get or create the category object
        product = Product.objects.create(category=category, **validated_data) # create the product object with the category
        return product

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category')