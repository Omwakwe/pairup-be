from django.conf.urls import url, include
from . import views
from rest_framework import routers
#from .views import LoginAPIView
from .models import Account
#from .serializers import LoginSerializer

router = routers.DefaultRouter()
router.register('students',views.StudentView, basename='students')
router.register('mentors',views.MentorView, basename='mentors')
router.register('admin',views.AdminView, basename='admins')
#router.register('login',views.LoginAPIView, basename='login')
#url(r'^/users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list')
#url('login/', LoginAPIView.as_view(), name='user-login'),

urlpatterns = [
   #url('login/', LoginAPIView.as_view(queryset = ''), name='user-login'),

]+router.urls