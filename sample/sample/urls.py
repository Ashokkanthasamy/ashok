from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logo.urls')),  # Make sure 'logo' is your app name
]
