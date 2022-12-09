from django.db import models
from datetime import date
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug          = models.CharField(max_length=1000, null=True, blank=True)
    is_available  = models.BooleanField(default=False)
    created_date  = models.DateTimeField(auto_now_add=True)
    update_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)



class Blog(models.Model):
    name             = models.CharField(max_length=100)
    images           = models.ImageField(upload_to='photos/blog', null=True, blank=True)
    image_url        = models.TextField(null=True, blank=True)
    # author         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mini_description = models.TextField()
    description      = RichTextUploadingField()
    is_available     = models.BooleanField(default=False)
    category         = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug             = models.CharField(max_length=1000, null=True, blank=True)
    created_date     = models.DateTimeField(auto_now_add=True)
    update_date      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name #+ " ==> " + str(self.author)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) #+ "-" + str(self.created_date))
        return super().save(*args, **kwargs)
    
    def get_url(self):
        return reverse('blog_detail', args=[self.category.slug, self.slug])
    
    def get_category(self):
        return reverse('blog_category', args=[self.category.slug])

