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
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('accounts.urls')),
    url(r'', include('cohort.urls')),
    url('api-auth/', include('rest_framework.urls')),
    #url('api/token/', CustomTokenObtainPairView.as_view(),
        #name='token_obtain_pair')
    #url('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #url('api/token/', TokenObtainPairView.as_view()),
    #url('api/token/refresh/', TokenRefreshView.as_view())
]
    #url(r'^user_login/$',views.user_login,name='user_login'),
    #url(r'^accounts/login/$',views.user_login,name='user_login'),
    #url(r'^logout/$', views.user_logout, name='user_logout'),


