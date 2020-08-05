from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import CohortSerializer
from .models import Cohort

class CohortView(viewsets.ModelViewSet):
    '''
    A view that creates,read,update and deletes a cohort(MC28)
    '''
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer
    permission_classes = (permissions.AllowAny,)




