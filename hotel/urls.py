"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rooms import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-bookings/', views.all_bookings, name='all-bookings'),
    path('create-booking/', views.create_booking, name='create-booking'),
    path('all-users/', views.get_all_users, name='all-users'),
    path('delete-booking/', views.delete_booking, name='delete-booking'),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
