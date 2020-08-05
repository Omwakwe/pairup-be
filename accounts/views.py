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
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt import authentication

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    @classmethod
    def get_extra_actions(cls):
        return []    

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



# class CreatePairs(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     authentication_classes = [authentication.JWTAuthentication]
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         day_of_week = "2020-8-5"
#         cohort_id = 2
#         retrived_cohort = Cohort.objects.get(id=cohort_id)
#         students_cohort = Account.objects.filter(is_student=True, cohort=retrived_cohort)
#         all_students = []
#         for student in students_cohort:
#             student_id = student.id
#             all_students.append(student_id)
#         print('student id')
#         print(all_students)
        
#         response = {'message': 'message'}
#         return Response(response)




