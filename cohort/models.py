from django.db import models


# Create your models here.
class Cohort(models.Model):
    cohort_name = models.CharField(max_length=30, unique=False)
    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)

    def __str__(self):
        return self.cohort_name

    class Meta:
        verbose_name_plural = 'cohort'

    
    


