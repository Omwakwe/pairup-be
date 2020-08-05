from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import CreatePairs


urlpatterns = [
    url('pair/', CreatePairs.as_view(), name='create_pairs'),
]

