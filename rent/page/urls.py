from django.urls import path
from . import views

urlpatterns = [

	path('', views.index, name='index'),
	path('voitures/', views.cars, name='cars'),
	path('services/', views.services, name='services'),
	path('contact/', views.contact, name='contact'),
	path('search/', views.search, name='search'),


]