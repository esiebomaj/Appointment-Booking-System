from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from .views import register_view

urlpatterns = [
    path('signup/', register_view, name='signup'),
    path('', include(auth_urls)),
]
