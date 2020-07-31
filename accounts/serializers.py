from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .managers import *

<<<<<<< HEAD

class UserSerializer(serializers.ModelSerializer):
    # users = serializers.PrimaryKeyRelatedField(many=True, queryset=Account.objects.all())
    class Meta:
        model = Account
        fields = ['id', 'email', 'password']


=======
>>>>>>> 2689108a511e7dcba82c7198d61d3df2032b3901
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ['id','email','first_name','last_name','user_name','bio','phone','last_login',]

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



    

