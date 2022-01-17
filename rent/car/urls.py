from django.urls import path
from .views import car_detail

app_name = 'car'

urlpatterns = [

	# path('', car, name='vehicle'),
	path('<slug:slug>/', car_detail, name='car_detail'),

]