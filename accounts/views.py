from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from rest_framework import viewsets
from .serializers import *
from .models import Account
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from .helper.email_helper import send_email
from django.template.loader import render_to_string
from rest_framework import status
from django.conf import settings
from rest_framework.response  import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_student=True)
    serializer_class = StudentSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class MentorView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_tm=True)
    serializer_class = MentorSerializer

class AdminView(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_admin=True, is_superuser=True)
    serializer_class = AdminSerializer
    
#Create your views here.
#def index(request):
    #return render(request, 'index.html',)


#def user_login(request):
    
    #if request.method == "POST":
        #username = request.POST.get("username")
        #password = request.POST.get("password")

        #user = authenticate(username=username, password=password)

        #if user:

            #if user.is_active:
                #login(request, user)

                #return HttpResponseRedirect(reverse("index"))
            #else:
                #return HttpResponseRedirect(reverse("user_login")) #raise error/ flash

        #else:
            #return HttpResponseRedirect(reverse("user_login")) #raise error/ flash
    #else:
        #return render(request, "auth/login.html", context={})


##@login_required
#def user_logout(request):
    #logout(request)
    #return HttpResponseRedirect(reverse("user_login"))
