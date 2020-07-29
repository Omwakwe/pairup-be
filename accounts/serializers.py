from rest_framework import serializers
from .models import Account
from .managers import *

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ['id','email','first_name','last_name','user_name','is_tm','is_student','is_superuser','is_active','is_staff','cohort','bio','phone','last_login',]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        # fields = '__all__'
        fields = ['id','email','first_name','last_name','user_name','cohort','bio','phone','last_login',]

        # email = serializers.EmailField()
        # username = serializers.CharField(max_length=20)
    

    def create(self, validated_data):
        validated_data['password'] = 'password'
        return Account.objects.create_student(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('content', instance.username)
        instance.save()
        return instance




    
