from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .serializers import AccountSerializer, CustomTokenObtainPairSerializer
from .serializers import *
from .models import Account
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer    

        

class MentorView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_tm=True)
    serializer_class = MentorSerializer


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class AdminView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_admin=True, is_superuser=True)
    serializer_class = AdminSerializer
    
class StudentView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_student=True)
    serializer_class = StudentSerializer




