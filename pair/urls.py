"""pair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from accounts import views
<<<<<<< HEAD
from django.urls import path

urlpatterns = [
    # url(r'', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'api/account/', include('accounts.urls')),
    url(r'api/cohorts/', include('cohort.urls')),
=======
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # url(r'', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('accounts.urls')),
    url(r'', include('cohort.urls')),
    url('api-auth/', include('rest_framework.urls')),
    url(r'api/account/', include('accounts.urls')),
    url(r'api/cohorts/', include('cohort.urls')),
]
    
>>>>>>> 2689108a511e7dcba82c7198d61d3df2032b3901



