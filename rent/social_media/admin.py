from django.contrib import admin
from .models import Social  
# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    list_display = ['facebook_link', 'twitter_link']
    list_display_links = ['facebook_link']

admin.site.register(Social, SocialAdmin)
