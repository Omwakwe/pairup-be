from django.db import models
# from studentpair.models import *


# Create your models here.
class Cohort(models.Model):
    cohort_name = models.CharField(max_length=30, unique=True)
    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    # pairs = models.OneToOneField(StudentPair, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pairs

    class Meta:
        verbose_name_plural = 'cohort'

    


