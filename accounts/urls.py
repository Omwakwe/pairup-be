from django.conf.urls import url
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('accounts',views.StudentView)

urlpatterns = [
    url(r"", include(router.urls)),
     
]