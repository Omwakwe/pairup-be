from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cohort.models import Cohort 
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _ 
from .managers import CustomUserManager
from django.utils.timezone import datetime, timedelta


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
	@property
	def token(self):
		date = datetime.now() + timedelta(hours=24)
		payload = {
            'email': self.email,
			'bio': self.bio,
			'phone ': self.phone,
            'exp': int(date.strftime('%s')),
            'id': self.id,
            'is_admin': self.is_admin,
            'is_tm': self.is_tm,
            'is_student': self.is_student,
        }
		token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
		return token.decode()

