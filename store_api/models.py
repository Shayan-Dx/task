from django.db import models


class Category(models.Model):
    title = models.CharField('title', max_length=20)
    description = models.TextField('description', blank=True)
    is_enable = models.BooleanField('is enable', default=True)
    created_time = models.DateTimeField('created time', auto_now_add=True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField('title', max_length=20)
    description = models.TextField('description', blank=True)
    is_enable = models.BooleanField('is enable', default=True)
    category = models.ForeignKey('Category', verbose_name='category', on_delete=models.CASCADE, blank=True, null=True)
    created_time = models.DateTimeField('created time', auto_now_add=True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title