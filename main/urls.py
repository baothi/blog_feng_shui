from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="blog_home"),
    path('/<slug:category_slug>/<slug:blog_slug>/',views.blog_detail, name='blog_detail'),
    path('/<slug:category_slug>/',views.blog_category, name='blog_category'),
    path("contact_us/", views.contactUs, name="contact_us"),
    
]
