from django.conf.urls import url, include
from . import views
from rest_framework import routers
from accounts.views import CustomTokenObtainPairView

router = routers.DefaultRouter()
router.register('accounts',views.AccountView)

urlpatterns = [
    url('', include(router.urls)),
    url('auth/jwt/token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    #url(r"^$", views.index, name="index"),
    #url(r"^profile/(\d+)", views.profile, name="profile"), 
]