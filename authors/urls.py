from django.urls import path
from authors import views

urlpatterns = [
    path('login/', views.logIn, name="login"),
    path('create-new-account/', views.signUp, name="register"),
   
]
