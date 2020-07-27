from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CohortSerializer
from .models import Cohort

class CohortView(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer

