from django.shortcuts import render, redirect
from .models import *
from .forms import ProductCommentForm
from django.contrib import messages


# Create your views here.

def product_detail(request, category_slug,product_slug):
  detail_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
  form = ProductCommentForm()
  if request.method == "POST":
    form = ProductCommentForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Yêu Cầu Tư Vấn Sản Phẩm " + detail_product.product_name + " thành công ")
        return redirect('/store/'+category_slug+'/'+product_slug)
  else:
      form = ProductCommentForm()
  # # Get the product gallery
  product_gallery = ProductGallery.objects.filter(product_id=detail_product.id)
  context = {
    'detail_product':detail_product,
    'form': form,
    'product_gallery':product_gallery,
  }
  return render(request, "store/product_detail.html", context)