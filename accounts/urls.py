from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('accounts',views.AccountView)

urlpatterns = [
    url('', include(router.urls)),

    # url('', include(router.urls))

    
    #url(r"^$", views.index, name="index"),
    #url(r"^profile/(\d+)", views.profile, name="profile"), 
]