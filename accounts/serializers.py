from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email','first_name','last_name','user_name','is_tm','is_student','is_superuser','is_active','is_staff','cohort','bio','phone','last_login',]
