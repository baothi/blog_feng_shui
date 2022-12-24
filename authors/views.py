import django
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignupForm, LoginUserForm, PasswordChangingForm , EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from main.models import Blog
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def signUp(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Bạn đăng ký Account Thành Công")
      new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
      login(request, new_user)
      return redirect('blog_home')
    else:
      messages.error(request, "Error")
  else:
    form = SignupForm()
  return render(request, "authors/register.html", {'form': form})

def logIn(request):
  if request.method == "POST":
    form = LoginUserForm(request, data = request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      remember_me = form.cleaned_data.get('checkbox')

      user = authenticate(username = username, password=password)

      if user is not None:
        login(request, user)
        if not remember_me:
          request.session.set_expiry(0)  # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.

                # else browser session will be as long as the session  cookie time "SESSION_COOKIE_AGE"
        messages.success(request, f"You are logged in as {username}")
        return redirect('blog_home')
      else:
        messages.error(request, "Error")
    else:
      messages.error(request, "Username or password incorrect")
  form = LoginUserForm()
  return render(request, "authors/login.html", {"form": form})

def logOut(request):
  logout(request)
  messages.success(request, "You have successfully logged out.")
  return redirect('blog_home')


@login_required(login_url="login")
def profile(request, user_name):
  user_related_data = Blog.objects.filter(author__username = user_name).filter(is_available=True).order_by('-created_date')
  page = request.GET.get('page', 1)
  paginator = Paginator(user_related_data, 10)
  try:
      user_related_data = paginator.page(page)
  except PageNotAnInteger:
      user_related_data = paginator.page(1)
  except EmptyPage:
      user_related_data = paginator.page(paginator.num_pages)
  except Exception as e:
      raise e
  context = {
      "user_related_data": user_related_data
  }
  return render(request, "authors/profile.html", context)

class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'login'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, "authors/password_change_success.html")

class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    login_url = 'login'
    template_name = "authors/edit_user_profile.html"
    success_url = reverse_lazy('blog_home')
    success_message = "User updated"

    def get_object(slef):
        return slef.request.user
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "kiểm tra dữ liệu đầy đủ trước khi submit")
        return redirect('blog_home')



