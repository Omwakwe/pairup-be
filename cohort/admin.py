from django.contrib import admin
from .models import *


class CohortAdmin(admin.ModelAdmin):
    list_display = ('cohort_name', 'date_added')



admin.site.register(Cohort, CohortAdmin)
