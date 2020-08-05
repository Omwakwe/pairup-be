from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .models import Account
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt import authentication


class CreatePairs(APIView):
    """
    View to list all students in the cohort.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        day_of_week = "2020-8-5"
        cohort_id = 2
        retrived_cohort = Cohort.objects.get(id=cohort_id)
        students_cohort = Account.objects.filter(is_student=True, cohort=retrived_cohort)
        all_students = []
        for student in students_cohort:
            student_id = student.id
            all_students.append(student_id)
        print('student id')
        print(all_students)
        
        response = {'message': 'message'}
        return Response(response)