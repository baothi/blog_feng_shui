from django.urls import path,re_path
from main import views

urlpatterns = [
    path("", views.home, name="blog_home"),
    path('/<slug:category_slug>/<slug:blog_slug>/',views.blog_detail, name='blog_detail'),
    path('/<slug:category_slug>/',views.blog_category, name='blog_category'),
    path("contact_us/", views.contactUs, name="contact_us"),
    path('create_new_blog/', views.CreateBlog.as_view(), name="create-blog"),
    path('update_blog/<int:pk>/', views.UpdateBlogView.as_view(), name="UpdateBlogView"),

    re_path(r'^delete_blog/(?P<id>[0-9]+)$', views.delete_blog, name="delete_blog"),
    # re_path(r'^congiap_sua/(?P<congiap_id>[0-9]+)$', views.congiap_sua, name='congiap_sua'),
    
]
