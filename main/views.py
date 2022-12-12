from django.shortcuts import redirect, render
from .models import *
from .forms import ContactForm, CreateBlogForm, UpdateBlogForm, CommentBlogForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import JsonResponse
from json import dumps
import json
from django.db.models import Count
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


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
        latest_news = Blog.objects.filter(is_available=True).filter(category__is_available=True).order_by('-created_date')[:4]
        list_json = list(latest_news.values('images','image_url'))
        dataJSON = dumps(list_json)
        all_comments = BlogComment.objects.filter(blog = detail.id)
        form = CommentBlogForm()
        if request.method == "POST":
            form = CommentBlogForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your comment on this blog has been posted")
                return redirect('/%2F'+detail.category.slug+'/'+detail.slug)
        else:
            form = CommentBlogForm()
    except Exception as e:
        raise e
#     # print(detail.description)
    context = {
        "detail": detail,
        "latest_news": latest_news,
        'data': dataJSON,
        'form': form,
        'all_comments': all_comments
    }
    return render(request,"main/blog_detail.html", context)

def blog_category(request,category_slug):
    latest_news = Blog.objects.filter(is_available=True).filter(category__is_available=True).order_by('-created_date')[:4]
    list_json = list(latest_news.values('images','image_url'))
    dataJSON = dumps(list_json)
    category_list = Blog.objects.filter(is_available=True).filter(category__slug=category_slug).order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(category_list, 10)
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
        "category_name": category_name,
        "latest_news": latest_news,
        'data': dataJSON,
    }
    return render(request,"main/category.html", context)

def contactUs(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bạn đã gởi yêu cầu thành công")
            return redirect("blog_home")
            
    else:
        form = ContactForm()
        messages.success(request, "vui lòng điền vào hồ sơ chi tiết")
    return render(request, "main/contact_us.html", {"form": form})


class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CreateBlogForm
    template_name = "main/create_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has been created"

class UpdateBlogView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Blog
    form_class = UpdateBlogForm
    template_name = "main/update_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has been updated"

@login_required(login_url="login")
def delete_blog(request ,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.is_available = False
    delete_blog.save()
    return HttpResponseRedirect("authors/user-profile/")




