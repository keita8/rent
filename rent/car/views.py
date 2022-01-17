from django.shortcuts import render, get_object_or_404
from .models import Car
from django.http import Http404

# Create your views here.

def car_detail(request, slug):

	single_car = get_object_or_404(Car, slug=slug)

	template_name = 'cars/car_detail.html'

	context = {

		'single_car': single_car,
	}
	
	return render(request, template_name, context)

def page_not_found(request, exception):
	template_name = '404.html'
	return render(request, template_name)
	

