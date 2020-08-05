from django.db import models
from cohort.models import Cohort
from accounts.models import *


# Create your models here.
class StudentPair(models.Model):
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')
    first_student = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='first_student')
    second_student = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='second_student')
    third_student = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return str(self.first_student.id) + ' ' + str(self.second_student.id)

    class Meta:
        verbose_name_plural = 'pairing'
