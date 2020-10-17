from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
