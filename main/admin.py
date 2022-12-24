from django.contrib import admin
from .models import Blog , Category, Contact, BlogComment

class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'is_available')

class BlogAdmin(admin.ModelAdmin):
  list_filter = ['category','is_available']
  search_fields = ['name','category__category_name']
  list_display = ('name','images', 'is_available', 'category')
  
  readonly_fields = ('created_date', 'update_date')
  list_per_page = 25

class CommentAdmin(admin.ModelAdmin):
  list_display = ('blog','author', 'comment_date')
  

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact)
admin.site.register(BlogComment,CommentAdmin)
