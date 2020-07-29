from rest_framework import serializers
from .models import Account
from .managers import *
from django.contrib.auth import authenticate



class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account

        fields = ['id','email','password','first_name','last_name','user_name','cohort','bio','phone','last_login',]

    
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

        fields = ['id','email','password','first_name','last_name','user_name','cohort','bio','phone','last_login',]

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

        fields = ['id','email','password','first_name','last_name','user_name','cohort','bio','phone','last_login',]

    def create(self, validated_data):
        validated_data['password'] = 'password'
        return Account.objects.create_admin(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('content', instance.username)
        instance.save()
        return instance


# class LoginSerializer(serializers.Serializer):
#     """Login serializer Class"""
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#     @staticmethod
#     def validate(data):
#         email = data.get('email', None)
#         password = data.get('password', None)
#         # As mentioned above, an email is required. Raise an exception if an
#         #email is not provided.
#         if email is None:
#             raise serializers.ValidationError(
#                 'An email is required to log in.'
#             )
#         # As mentioned above, a password is required. Raise an exception if a
#         # password is not provided.
#         if password is None:
#             raise serializers.ValidationError(
#                 'A password is required to log in.'
#             )
#         # The `authenticate` method is provided by Django and handles checking
#         # for a user that matches this email/password combination. Notice how
#         # we pass `email` as the `email value. Remember that, in our User
#         # model, we set `USERNAME_FIELD` as `email`.
#         user = authenticate(email=email, password=password)
#         # If no user was found matching this user_name/password combination then
#         # `authenticate` will return `None`. Raise an exception in this case.
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password was not found.'
#             )
#         # The `validate` method should return a dictionary of validated data.
#         # This is the data that is passed to the `create` and `update` methods
#         # that we will see later on.
#         return {
#             'email':user.email,
#             'token': user.token,
#         }
         
    
