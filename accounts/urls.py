from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('students',views.StudentView, basename='students')
router.register('mentors',views.MentorView, basename='mentors')
router.register('admins',views.AdminView, 'admin')

urlpatterns = []+router.urls