from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from accounts.models import Account
from cohort.models import Cohort
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from .serializers import StudentPairSerializer
import pendulum
import requests
import json

class CreatePairs(APIView):
    """
    View to list all students in the cohort.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentPairSerializer

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
    
        day_of_week = request.POST["day_of_week"]
        cohort_id = request.POST["cohort_id"]
        print("day_of_week",day_of_week)
        print("cohort_id",cohort_id)
        day_of_week_list = day_of_week.split("-")
        print("day_of_week_list",day_of_week_list)

        pendulum_date = pendulum.datetime(int(str(day_of_week_list[0])),int(str(day_of_week_list[1])),int(str(day_of_week_list[2])))
        start_date = pendulum_date.start_of('week')
        end_date = pendulum_date.end_of('week')

        print("start_date",start_date)
        print("end_date",end_date)

        retrived_cohort = Cohort.objects.get(id=cohort_id)
        students_cohort = Account.objects.filter(is_student=True, cohort=retrived_cohort)
        all_students = []
        for student in students_cohort:
            student_id = student.id
            all_students.append(student_id)
        print('student id')
        print(all_students)
        response = {'student_id':'student_id'}
        # response = requests.get(cohort_id)
        # print(response.status_code)
        # my_json =response.json()
        # print(json.dumps(my_json,indent=2,sort_keys=True))
        return Response(response)
        # dt = pendulum.datetime(2020, 8, 5)

        # start_date = dt.start_of('week')
        # end_date = dt.end_of('week')