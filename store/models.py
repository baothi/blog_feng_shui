from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import string
import random

# Create your models here.

class Category_Product(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug          = models.CharField(max_length=1000, null=True, blank=True)
    description   = models.TextField(max_length=255, blank=True)
    # cat_image   = models.ImageField(upload_to='photos/categories', blank=True)
    images        = models.ImageField(upload_to='photos/categories', null=True, blank=True)
    image_url     = models.TextField(null=True, blank=True)
    is_available    = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name    = models.CharField(max_length=500, unique=True)
    slug            = models.CharField(max_length=500, null=True, blank=True)
    sku             = models.CharField(max_length=14, blank=True)
    description     = RichTextUploadingField()
    mini_description= models.TextField(null=True, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products', null=True, blank=True)
    image_url       = models.TextField(null=True, blank=True)
    stock           = models.IntegerField()
    discount        = models.IntegerField(null=True, blank=True)
    is_available    = models.BooleanField(default=False)
    category        = models.ForeignKey(Category_Product, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
      return reverse('product_detail', args=[self.category.slug, self.slug])

    def get_product(self):
      return reverse('store', args=[self.id, self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        if not self.sku:
            size=6 
            chars=string.digits
            self.sku = 'THEZOO' + ''.join(random.choice(chars) for _ in range(size))
        return super().save(*args, **kwargs)

    def __str__(self):
      return self.product_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category  = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value     = models.CharField(max_length=100)
    is_active           = models.BooleanField(default=True)
    created_date        = models.DateTimeField(auto_now=True)

    objects             = VariationManager()

    def __str__(self):
        return self.variation_value

# class ReviewRating(models.Model):
#     product    = models.ForeignKey(Product, on_delete=models.CASCADE)
#     author     = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     subject    = models.CharField(max_length=100, blank=True)
#     review     = models.TextField(max_length=1500, blank=True)
#     rating     = models.FloatField()
#     ip         = models.CharField(max_length=20, blank=True)
#     status     = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.subject


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='store/products', max_length=255)
    image          = models.ImageField(upload_to='store/products', null=True, blank=True)
    image_url       = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'

class ProductComment(models.Model):
    name         = models.CharField(max_length=200)
    e_mail       = models.EmailField(max_length=250)
    phone_number = models.IntegerField()
    subject      = models.CharField(max_length=500)
    description  = models.TextField(help_text="viết Yêu Cầu Tư Vấn")
    comment_date = models.DateTimeField(auto_now_add=True)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)