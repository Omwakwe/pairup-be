from rest_framework import serializers
from .models import Cohort

class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = ['id','cohort_name','date_added']


# Pair record modul

# date 
# student1 & 2
# cohort 