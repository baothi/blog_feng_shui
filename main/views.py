from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import JsonResponse
from json import dumps
import json
from django.db.models import Count
# Create your views here.


def home(request):
    baiviet1chinh = Blog.objects.filter(is_available=True).filter(category__is_available=True).order_by('?')[:1]
    baiviet2chinh = Blog.objects.filter(is_available=True).filter(category__is_available=True).order_by('?')[2:3]
    baiviet3chinh = Blog.objects.filter(is_available=True).filter(category__is_available=True).order_by('?')[1:3]
    kinhdich1 = Blog.objects.filter(is_available=True).filter(category__is_available=True).filter(category__slug="kinh-dich").order_by('?')[1:3]
    kinhdich2 = Blog.objects.filter(is_available=True).filter(category__is_available=True).filter(category__slug="kinh-dich").order_by('-created_date')[:5]
    
    tuvi1 = Blog.objects.filter(is_available=True).filter(category__is_available=True).filter(category__slug="tu-vi").order_by('?')[2:3]
    tuvi2 = Blog.objects.filter(is_available=True).filter(category__is_available=True).filter(category__slug="tu-vi").order_by('-created_date')[:3]
    battu = Blog.objects.filter(is_available=True).filter(category__is_available=True).filter(category__slug="bat-tu").order_by('-created_date')[:9]
    latest_news = Blog.objects.filter(is_available=True).filter(category__is_available=True).order_by('-created_date')[:5]
    list_json = list(latest_news.values('images','image_url'))
    dataJSON = dumps(list_json)
    context = {
        "baiviet1chinh": baiviet1chinh,
        "baiviet2chinh": baiviet2chinh,
        "baiviet3chinh": baiviet3chinh,
        "kinhdich1": kinhdich1,
        "kinhdich2": kinhdich2,
        "tuvi1": tuvi1,
        "tuvi2": tuvi2,
        "battu": battu,
        "latest_news": latest_news,
        'data': dataJSON,
    }
    return render(request, "main/home.html", context)

def blog_detail(request,category_slug,blog_slug):
    try:
        detail = Blog.objects.get(category__slug=category_slug, slug=blog_slug)
    except Exception as e:
        raise e
#     # print(detail.description)
    context = {
        "detail": detail
    }
    return render(request,"main/blog_detail.html", context)

def blog_category(request,category_slug):
    category_list = Blog.objects.filter(is_available=True).filter(category__slug=category_slug).order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(category_list, 2)
    try:
        category = paginator.page(page)
        category_name = Category.objects.get(slug=category_slug)
    except PageNotAnInteger:
        category = paginator.page(1)
    except EmptyPage:
        category = paginator.page(paginator.num_pages)
    except Exception as e:
        raise e
    print(category)
    context = {
        "category": category,
        "category_name": category_name
    }
    return render(request,"main/category.html", context)
