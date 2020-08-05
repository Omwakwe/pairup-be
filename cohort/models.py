from django.db import models
from accounts.models import *
# from studentpair.models import *


# Create your models here.
class Cohort(models.Model):
    cohort_name = models.CharField(max_length=30, unique=True)
    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    members = models.ManyToOneRel(Account, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.cohort_name

    class Meta:
        verbose_name_plural = 'cohort'

    


