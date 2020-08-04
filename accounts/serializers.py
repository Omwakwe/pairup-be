from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .managers import *
from .password import generate_password
from rest_framework_simplejwt.tokens import RefreshToken
from cohort.serializers import *
# from cohort.serializers import *

class AccountSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Account
        fields = ['id','email','first_name','last_name','user_name','bio','phone','last_login',]
        
class StudentSerializer(serializers.ModelSerializer):
    cohort = serializers.ReadOnlyField(source='cohort.cohort_name')
    
    class Meta:
        model = Account
        fields = ['id','email','first_name','last_name','user_name', 'cohort','bio','phone','last_login',]

    def create(self, validated_data):
        validated_data['password'] = generate_password(8)
        print('Create student')
        return Account.objects.create_student(**validated_data)


    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('content', instance.username)
        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['email'] = user.email
        token['bio'] = user.bio
        token['phone'] = user.phone



        

        

        if user.is_admin:
            token['role'] = 'admin'
        elif user.is_tm:
            token['role'] = 'mentor'
        elif user.is_student:
            token['role'] = 'student'
        else:
            token['role'] = 'Unknown'


        return token


        fields = ['id','email','first_name','last_name','user_name','cohort','bio','phone','last_login',]

class MyTokenObtainPairSerializer(CustomTokenObtainPairSerializer):
    # @classmethod
    # def get_token(cls, user):
    #     return RefreshToken.for_user(user)

    def validate(self, attrs):
        token = super().validate(attrs)

        refresh = self.get_token(self.user)

        token['refresh'] = str(refresh)
        token.pop('access', None) # remove access from the payload
        
        

        return token

class MentorSerializer(serializers.ModelSerializer):
    cohort = serializers.ReadOnlyField(source='cohort.cohort_name')

    class Meta:
        model = Account

        fields = ['id','email','first_name','last_name','user_name','cohort','bio','phone','last_login',]

    def create(self, validated_data):
        validated_data['password'] = generate_password(8)
        return Account.objects.create_tm(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('content', instance.username)
        instance.save()
        return instance


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = ['id','email','first_name','last_name','user_name','bio','phone','last_login',]

    def create(self, validated_data):
        validated_data['password'] = 'password'
        return Account.objects.create_admin(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('content', instance.username)
        instance.save()
        return instance



    
