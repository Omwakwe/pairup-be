from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets, generics, mixins
from .serializers import *
from .models import Account
from rest_framework.permissions import AllowAny


class MentorView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_tm=True)
    serializer_class = MentorSerializer

class AdminView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_admin=True, is_superuser=True)
    serializer_class = AdminSerializer
    
class StudentView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_student=True)
    serializer_class = StudentSerializer

# class LoginAPIView(generics.CreateAPIView):
#     # Login user class
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer
#     def post(self, request):
#         """
#         Handle user signup
#         """
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)  

