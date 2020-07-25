from django.db import models
from accounts.models import Account


# Create your models here.
class Cohort(models.Model):
    cohort_name = models.CharField(max_length=30, unique=False)
    student = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'cohort'
    

    def __str__(self):
        return self.cohort_name


