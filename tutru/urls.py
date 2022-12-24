from django.urls import include, path
from . import views

urlpatterns = [
    # … other patterns
    path('', views.index, name='tutru'),
    # … other patterns
]