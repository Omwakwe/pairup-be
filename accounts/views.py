from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .serializers import AccountSerializer
from .models import Account



class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

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
