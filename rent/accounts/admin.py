from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'last_login', 'date_joined', 'is_active')
	filter_horizontal = ()
	readonly_fields = ('last_login', 'date_joined')
	list_display_links = ('email', 'username')
	list_filter = ('email','username')
	fieldsets = ()
	ordering = ('-date_joined', )

admin.site.register(Account, AccountAdmin)