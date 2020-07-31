from rest_framework import serializers
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AccountSerializer(serializers.ModelSerializer):
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
