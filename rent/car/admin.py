from django.contrib import admin
from .models import Car, Banner
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):

	def thumbnail(self, object):
		return format_html('<img src="{}" width="40" style="border-radius: 50px;">'.format(object.photo.url))

	thumbnail.short_description = 'Photo'


	list_display_links = ['thumbnail', 'car_title']
	list_display = ['thumbnail' ,'car_title','color', 'modele', 'condition','body_style','fuel', 'price', 'year', 'for_sale', 'is_featured']
	search_fields = ['car_title', 'condition', 'modele', 'year', 'price']
	prepopulated_fields = {'slug':('car_title', )}
	list_editable = ('is_featured', 'for_sale')
	list_filter = ('condition', 'body_style', 'modele', 'car_title', 'fuel')


class BannerAdmin(admin.ModelAdmin):
	list_display = ['title']
	list_filter = ['title']
	

admin.site.register(Car, CarAdmin)
admin.site.register(Banner, BannerAdmin)