"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path("", include("audience.urls")),
    path("predict/", include("predict.urls")),
    path("user_profile/", include("user_profile.urls")),

    path("accounts/register/", views.register, name="register"),
    path('accounts/login/', views.custom_login, name='custom_login'),
    # path('updateprofile/', views.update_profile, name='update_profile'),
    path('accounts/logout/', views.custom_logout, name='custom_logout'),
    path('accounts/', include('allauth.urls')),
    path("admin/", admin.site.urls),
]
