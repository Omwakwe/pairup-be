from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cohort.models import Cohort 
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _ 
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from journal.settings import AUTH_USER_MODEL as User


class Account(AbstractBaseUser, PermissionsMixin):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name 				= models.CharField(max_length=30, unique=False)
	last_name				= models.CharField(max_length=30, unique=False)
	user_name               = models.CharField(max_length=10, unique=True, default='')
	bio                     = models.TextField(blank=True)
	profile_pic             = CloudinaryField('profile_pic')
	cohort                  = models.ForeignKey(Cohort, on_delete=models.CASCADE, null=True)
	phone                   = models.CharField(max_length = 10,blank =True, unique=False)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=True)
	is_tm				    = models.BooleanField(default=False)
	is_student				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	ordering = ('email',)

	# objects = MyAccountManager()
	objects = CustomUserManager()


	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email_confirmed = models.BooleanField(default=False)
    reset_password = models.BooleanField(default=False)

    class Meta:
        app_label = 'auth'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
