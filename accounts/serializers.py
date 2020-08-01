from rest_framework import serializers
from .models import Account
from .managers import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account

        fields = ['id','email','first_name','last_name','user_name','cohort','bio','phone','last_login',]

    
    def create(self, validated_data):
        validated_data['password'] = 'password'
        return Account.objects.create_student(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('content', instance.username)
        instance.save()
        return instance

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = ['id','email','first_name','last_name','user_name','cohort','bio','phone','last_login',]

    def create(self, validated_data):
        validated_data['password'] = 'password'
        return Account.objects.create_tm(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('content', instance.username)
        instance.save()
        return instance


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = ['id','email','first_name','last_name','user_name','cohort','bio','phone','last_login',]

    def create(self, validated_data):
        validated_data['password'] = 'password'
        return Account.objects.create_admin(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('content', instance.username)
        instance.save()
        return instance



    
