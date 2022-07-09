"""TechieChandan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include,re_path

# for manage media files

# from django.conf.urls import re_path
# from django.conf.urls import url
# from django.conf.urls import url, include

from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # re_path(f'media/(?p<path>.*)&',),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


handler404 = 'blog.views.error_404_view'

#Admin Panel Titles Configuration
admin.site.site_header ="TechieChandan Administration"
admin.site.site_title ="TechieChandan Administration"
admin.site.index_title ="Wellcome To The TechieChandan Admin Pannel..."