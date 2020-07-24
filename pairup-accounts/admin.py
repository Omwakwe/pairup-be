from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_tm', 'is_student')
	list_editable=[ 'username', 'phone']

	search_fields = ('email', 'username',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)

