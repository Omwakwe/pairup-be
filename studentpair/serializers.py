from rest_framework import serializers

class StudentPairSerializer(serializers.Serializer):
    cohort_id = serializers.IntegerField()
    day_of_week = serializers.DateField()