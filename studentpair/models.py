from django.db import models
from cohort.models import Cohort
from accounts.models import *


# Create your models here.
class StudentPair(models.Model):
    start_date = models.DateField(verbose_name='start date')
    end_date = models.DateField(verbose_name='end date')
    first_student = models.ForeignKey(Account, on_delete=models.CASCADE)
    second_student = models.ForeignKey(Account, on_delete=models.CASCADE)
    third_student = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, null=False)

   
    def __str__(self):
        return self.cohort # F-String

    class Meta:
        verbose_name_plural = 'pairing'
