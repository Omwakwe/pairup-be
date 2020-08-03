from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ('email', 'first_name','last_name', 'user_name','cohort', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_tm', 'is_student','is_superuser',)
    list_filter = ('email', 'first_name','last_name', 'user_name', 'cohort', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_tm', 'is_student', 'is_superuser',) 
    fieldsets = (
        (None, {'fields': ('email', 'password' ,'first_name','cohort','last_name','user_name', 'phone',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_tm', 'is_student', 'is_admin', 'is_superuser','cohort',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name','last_name', 'user_name','phone','is_staff', 'is_active', 'is_tm', 'is_student', 'is_admin','cohort', )}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Account, CustomUserAdmin)




