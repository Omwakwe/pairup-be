# from django.conf.urls import url, include
from django.urls import path
from .views import CreatePairs, PairHistoryView, StudentPairView


urlpatterns = [
    path('pair/', CreatePairs.as_view(), name='create_pairs'),
    path('pair_history/', PairHistoryView.as_view(), name='pair_history'),
    path('new_student_pair/', StudentPairView.as_view(), name='new_student_pair'),
]

