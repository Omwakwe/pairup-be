from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import CustomTokenObtainPairView

router = routers.DefaultRouter()
router.register('students',views.StudentView, basename='students')
router.register('mentors',views.MentorView, basename='mentors')
router.register('admins',views.AdminView, basename='admins')
router.register('login',views.CustomTokenObtainPairView, basename='login')
router.register('cohorts',views.CohortStudentsView, basename='cohort')


urlpatterns = [
    
    url('', include(router.urls)),
    url('auth/jwt/token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),

    
]
