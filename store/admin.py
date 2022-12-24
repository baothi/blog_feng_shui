from django.contrib import admin

# Register your models here.
from .models import Category_Product, Product, Variation ,  ProductGallery ,ProductComment
import admin_thumbnails

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('subcategory_name',)}
    list_display = ('subcategory_name', 'slug','category')

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

# class Review(admin.ModelAdmin):
#     list_display = ('product', 'user', 'subject', 'rating', 'ip', 'updated_at')

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category','category__category_name']
    search_fields = ['product_name','category__category_name','sku']
    list_display = ('product_name', 'price','sku', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)

admin.site.register(ProductGallery)
admin.site.register(Category_Product,CategoryAdmin)
admin.site.register(ProductComment)