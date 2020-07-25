from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CohortAdmin(UserAdmin):
    list_display =('cohort_name')
    list_ediable =['cohort_name']

    list_display = ()  # Contain only fields in your `custom-user-model`
    list_filter = ()  # Contain only fields in your `custom-user-model` intended for filtering. Do not include `groups`since you do not have it
    search_fields = ()  # Contain only fields in your `custom-user-model` intended for searching
    ordering = ()  # Contain only fields in your `custom-user-model` intended to ordering
    filter_horizontal = ()

admin.site.register(Cohort, CohortAdmin)
