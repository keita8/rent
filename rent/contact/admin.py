from django.contrib import admin
from .models import Contact, About
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'last_name', 'first_name', 'phone', 'email', 'car_id', 'car_title', 'created_date']
	search_fields = ['last_name', 'first_name', 'email', 'car_title']
	list_display_links = ['last_name', 'first_name']
	list_per_page = 10


admin.site.register(Contact, ContactAdmin)
admin.site.register(About)