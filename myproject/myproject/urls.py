# myproject/urls.py
from django.contrib import admin
from django.urls import path, include  # Add 'include' to import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include the app's URLs
]
