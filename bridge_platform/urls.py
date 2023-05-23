"""bridge_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin, auth
from django.urls import path, include 
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('index_d/', TemplateView.as_view(template_name='index_d.html'), name='index_d'),
    path('index/', views.index, name='index'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('test/', TemplateView.as_view(template_name='test.html'), name='test'),
    path('test_2/', TemplateView.as_view(template_name='test_2.html'), name='test_2'),
    path('test_rotations/', TemplateView.as_view(template_name='test_rotations.html'), name='test_rotations'),
    path('rotations_62/', TemplateView.as_view(template_name='rotations_62.html'), name='rotations_62'),
    path('test_js/', TemplateView.as_view(template_name='test_js.html'), name='test_js'),
    path('test_css/', TemplateView.as_view(template_name='test_css.html'), name='test_css'),
    path('new_home/', TemplateView.as_view(template_name='new_home.html'), name='new_home')
]
