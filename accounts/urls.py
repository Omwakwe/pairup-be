from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('accounts',views.StudentView)
router.register('accounts',views.MentorView)
router.register('accounts',views.AdminView)

urlpatterns = [
    url('', include(router.urls))
    
]