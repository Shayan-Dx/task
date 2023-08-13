from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


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
    categories = models.ManyToManyField('Category', verbose_name='categories', blank=True)
    created_time = models.DateTimeField('created time', auto_now_add=True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
    

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users MUST have an email address!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    

class User(models.Model):
    email = models.EmailField('email', unique=True)
    name = models.CharField('name', max_length=25)
    is_active = models.BooleanField('is active', default=True)
    is_staff = models.BooleanField('is staff', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name
    
    def __str__(self):
        return self.email