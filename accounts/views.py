from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .serializers import *
from .models import Account
# from .token_generator import account_activation_token
from django.core.mail import send_mail

class MentorView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_tm=True)
    serializer_class = MentorSerializer

class AdminView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_admin=True)
    serializer_class = AdminSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_student=True)
    serializer_class = StudentSerializer

# #create views
def index(request):   
    send_mail('Hello from Moringa School',
    'Behold are your login credentials',
    'mdawidamengo@gmail.com',
    ['matokej569@fazmail.net'],
    fail_silently = False
    )
    return render(request, 'email/index.html')
