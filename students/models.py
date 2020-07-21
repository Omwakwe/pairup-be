from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic')
    phone_number = models.CharField(max_length = 10,blank =True)
    bio = models.TextField(blank=True)
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic')
    phone_number = models.CharField(max_length = 10,blank =True)
    bio = models.TextField(blank=True)
    course = models.ForeignKey(Module, on_delete=models.CASCADE)
    Sensei = models.ForeignKey(Mentor, on_delete=models.CASCADE)

class Module(models.Model):
    mod_name = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic')
    phone_number = models.CharField(max_length = 10,blank =True)
    bio = models.TextField(blank=True)