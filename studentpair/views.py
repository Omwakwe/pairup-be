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
from .serializers import StudentPairSerializer, SingleStudentSerializer
import pendulum
import requests
import json
from .models import StudentPair
from .functions import pairup
import copy
from django.db.models import Q


class StudentPairView(APIView):
    """
    View to get a single student pair.

    * Requires  JWT authentication.
    * Only authenticated students are able to access this view.
    """
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = SingleStudentSerializer

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        print("student pair view called")
        day_of_week = pendulum.now()
        # day_of_week = request.POST["day_of_week"]
        student_id = request.POST["student_id"]
        print('STUDENT ID', student_id)
        print("day_of_week",day_of_week)
        day_of_week = str(day_of_week)[0:10]
        
        day_of_week_list = day_of_week.split("-")
        print("day_of_week_list",day_of_week_list)

        # pendulum_date = pendulum.datetime(int(str(day_of_week_list[0])),int(str(day_of_week_list[1])),int(str(day_of_week_list[2])))
        pendulum_date = pendulum.now()
        start_date = pendulum_date.start_of('week')
        end_date = pendulum_date.end_of('week')
        formated_start_date = str(start_date)[0:10]
        formated_end_date = str(end_date)[0:10]
        print("start_date", formated_start_date)
        print("end_date",formated_end_date)
        my_pair = []
        if StudentPair.objects.filter(Q(start_date=formated_start_date, first_student_id=student_id)| Q(start_date=formated_start_date, second_student_id=student_id)| Q(start_date=formated_start_date, third_student_id=student_id)).exists():
            pair_exists = StudentPair.objects.filter(Q(start_date=formated_start_date, first_student_id=student_id)| Q(start_date=formated_start_date, second_student_id=student_id)| Q(start_date=formated_start_date, third_student_id=student_id))[0]
            print("Foud Pair", pair_exists )
            print("THIRD STUDENT", pair_exists.third_student)
            if pair_exists.third_student == None:
                print("HERE ONE", pair_exists.first_student_id, student_id)
                print("HERE ONE", pair_exists.second_student_id, student_id)
                if int(pair_exists.first_student_id) == int(student_id):
                    print("HERE TWO")
                    student = pair_exists.second_student
                    student_object = {}
                    student_object['email'] = student.email
                    student_object['first_name'] = student.first_name
                    student_object['last_name'] = student.last_name
                    student_object['phone'] = student.phone
                    my_pair.append(student_object)

                if int(pair_exists.second_student_id) == int(student_id):
                    print("HERE THREE")
                    student = pair_exists.first_student
                    student_object = {}
                    student_object['email'] = student.email
                    student_object['first_name'] = student.first_name
                    student_object['last_name'] = student.last_name
                    student_object['phone'] = student.phone
                    my_pair.append(student_object)
                print("HERE 4")

            if pair_exists.third_student != None:
                if int(pair_exists.first_student_id) == int(student_id):
                    student2 = pair_exists.second_student
                    student_object2 = {}
                    student_object2['email'] = student2.email
                    student_object2['first_name'] = student2.first_name
                    student_object2['last_name'] = student2.last_name
                    student_object2['phone'] = student2.phone
                    my_pair.append(student_object2)

                    student3 = pair_exists.third_student
                    student_object3 = {}
                    student_object3['email'] = student3.email
                    student_object3['first_name'] = student3.first_name
                    student_object3['last_name'] = student3.last_name
                    student_object3['phone'] = student3.phone
                    my_pair.append(student_object3)

                
                if int(pair_exists.second_student_id) == int(student_id):
                    student1 = pair_exists.first_student
                    student_object1 = {}
                    student_object1['email'] = student1.email
                    student_object1['first_name'] = student1.first_name
                    student_object1['last_name'] = student1.last_name
                    student_object1['phone'] = student1.phone
                    my_pair.append(student_object1)

                    student3 = pair_exists.third_student
                    student_object3 = {}
                    student_object3['email'] = student3.email
                    student_object3['first_name'] = student3.first_name
                    student_object3['last_name'] = student3.last_name
                    student_object3['phone'] = student3.phone
                    my_pair.append(student_object3)
                    
                if int(pair_exists.third_student_id) == int(student_id):
                    student1 = pair_exists.first_student
                    student_object1 = {}
                    student_object1['email'] = student1.email
                    student_object1['first_name'] = student1.first_name
                    student_object1['last_name'] = student1.last_name
                    student_object1['phone'] = student1.phone
                    my_pair.append(student_object1)

                    student2 = pair_exists.second_student
                    student_object2 = {}
                    student_object2['email'] = student2.email
                    student_object2['first_name'] = student2.first_name
                    student_object2['last_name'] = student2.last_name
                    student_object2['phone'] = student2.phone
                    my_pair.append(student_object2)
        print("MY PAIR", my_pair)

        response = {"data": my_pair}

        return Response(response)

class PairHistoryView(APIView):
    """
    View to retrive history of paired students in the cohort.

    * Requires JWT authentication.
    * Only authenticated TMs are able to access this view.
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
        formated_start_date = str(start_date)[0:10]
        formated_end_date = str(end_date)[0:10]
        print("start_date", formated_start_date)
        print("end_date",formated_end_date)
        retrived_cohort = Cohort.objects.get(id=cohort_id)
        pair_history = StudentPair.objects.filter(cohort=retrived_cohort, start_date=formated_start_date)
        pair_history_list = []
        for pair in pair_history:
            students = []
            
            student1 = pair.first_student
            student1_object = {}
            student1_object['email'] = student1.email
            student1_object['first_name'] = student1.first_name
            student1_object['last_name'] = student1.last_name
            student1_object['phone'] = student1.phone
            students.append(student1_object)

            student2 = pair.second_student
            student2_object = {}
            student2_object['email'] = student2.email
            student2_object['first_name'] = student2.first_name
            student2_object['last_name'] = student2.last_name
            student2_object['phone'] = student2.phone
            students.append(student2_object)

            if pair.third_student != None:
                student3 = pair.third_student
                student3_object = {}
                student3_object['email'] = student3.email
                student3_object['first_name'] = student3.first_name
                student3_object['last_name'] = student3.last_name
                student3_object['phone'] = student3.phone
                students.append(student3_object)
            pair_history_list.append(students)
        print("Pair History", pair_history_list)

        response = {"Data": pair_history_list}
        return Response(response)

class CreatePairs(APIView):
    """
    View to create students in the cohort.

    * Requires JWT authentication.
    * Only TMs are able to access this view.
    """
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = StudentPairSerializer

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        new_pairs = []
        day_of_week = request.POST["day_of_week"]
        cohort_id = request.POST["cohort_id"]
        print("day_of_week",day_of_week)
        print("cohort_id",cohort_id)
        day_of_week_list = day_of_week.split("-")
        print("day_of_week_list",day_of_week_list)

        pendulum_date = pendulum.datetime(int(str(day_of_week_list[0])),int(str(day_of_week_list[1])),int(str(day_of_week_list[2])))
        start_date = pendulum_date.start_of('week')
        end_date = pendulum_date.end_of('week')
        formated_start_date = str(start_date)[0:10]
        formated_end_date = str(end_date)[0:10]
        print("start_date", formated_start_date)
        print("end_date",formated_end_date)
        retrived_cohort = Cohort.objects.get(id=cohort_id)
        if StudentPair.objects.filter(cohort=retrived_cohort, start_date=formated_start_date).exists():
            response = {"ERROR": 'Pairs for that week already exists'}
            return Response(response)
        students_cohort = Account.objects.filter(is_student=True, cohort=retrived_cohort)

        Weeks = StudentPair.objects.order_by('start_date').distinct('start_date')
        print('WEEKS', Weeks)
        weeks_list = []
        for week in Weeks:
            weeks_list.append(week.start_date)
        print('WEEKS_LIST', weeks_list)
        pairing_history = []
        for each_week in weeks_list:
            one_week_history = []
            weekly_pairs = StudentPair.objects.filter(start_date = each_week)
            for week_pair in weekly_pairs:
                print('WEEK PAIR', each_week,week_pair)
                pair = []
                if week_pair.third_student == None:
                    first = week_pair.first_student_id
                    second = week_pair.second_student_id
                    pair.append(first)
                    pair.append(second)
                else:
                    first = week_pair.first_student_id
                    second = week_pair.second_student_id
                    third = week_pair.third_student_id
                    pair.append(first)
                    pair.append(second)
                    pair.append(third)
                    
                one_week_history.append(pair)
                print('ONE_WEEK_HIST', one_week_history)

            pairing_history.append(one_week_history)
            print('PAIRNG_WEEK_HIST', pairing_history)

        all_students = []
        for student in students_cohort:
            student_id = student.id
            all_students.append(student_id)
        print('student id', all_students)
        all_students_copy=copy.deepcopy(all_students)
        pairing_history_copy=copy.deepcopy(pairing_history)
        new_pairs = pairup(all_students_copy, pairing_history_copy)
        print('new pairs', new_pairs)
        for pair in new_pairs:
            new_student_pair = StudentPair()
            new_student_pair.start_date = formated_start_date
            new_student_pair.end_date = formated_end_date
            new_student_pair.cohort = retrived_cohort
        
            if len(pair) == 2:
                student1_id = pair[0]
                student2_id = pair[1]
                new_student_pair.first_student_id = student1_id
                new_student_pair.second_student_id = student2_id
            if len(pair) == 3:
                student1_id = pair[0]
                student2_id = pair[1]
                student3_id = pair[2]
                new_student_pair.first_student_id = student1_id
                new_student_pair.second_student_id = student2_id
                new_student_pair.third_student_id = student3_id
            new_student_pair.save()
        response = {'message': 'Successfully Created Pairs'}
        print("All students", all_students)
        return Response(response)
        
    
       
    