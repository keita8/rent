from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Team
from car.models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.mail import send_mail
from accounts.models import Account
import requests
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages

# Create your views here.
def index(request):

	team = Team.objects.all()
	featured = Car.objects.order_by('-created_date').filter(is_featured=True)
	all_cars = Car.objects.order_by('-created_date')
	model_search = Car.objects.values_list('modele', flat=True).distinct()
	transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
	body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
	year_search = Car.objects.values_list('year', flat=True).distinct()
	# search_fields = Car.objects.values('modele', 'year', 'body_style', 'city')

	template_name = 'page/index.html'
	context = {

	'team' : team,
	'featured' : featured,
	'all_cars' : all_cars,
	'model_search' : model_search,
	'transmission_search' : transmission_search,
	'body_style_search' : body_style_search,
	'year_search' : year_search

	}

	return render(request, template_name, context)




def services(request):
	return render(request, 'page/services.html', {})




def cars(request):

	cars = Car.objects.order_by('-created_date')
	paginator = Paginator(cars, 6)
	page = request.GET.get('page')
	paged_cars = paginator.get_page(page)
	model_search = Car.objects.values_list('modele', flat=True).distinct()
	transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
	body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
	year_search = Car.objects.values_list('year', flat=True).distinct()


	context = {
	'cars':paged_cars,
	'model_search' : model_search,
	'transmission_search' : transmission_search,
	'body_style_search' : body_style_search,
	'year_search' : year_search
	}

	return render(request, 'page/cars.html', context)


def search(request):

	cars = Car.objects.order_by('-created_date')

	model_search = Car.objects.values_list('modele', flat=True).distinct()
	city_search = Car.objects.values_list('city', flat=True).distinct()
	body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
	year_search = Car.objects.values_list('year', flat=True).distinct()
	transmission_search = Car.objects.values_list('transmission', flat=True).distinct()


	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			cars = cars.filter(
				Q(car_title__icontains=keyword) | Q(description__icontains=keyword)
				)

	if 'modele' in request.GET:
		modele = request.GET['modele']
		if modele:
			cars = cars.filter(

				modele__iexact=modele

				)

	if 'transmission' in request.GET:
		transmission = request.GET['transmission']
		if transmission:
			cars = cars.filter(
				transmission__iexact=transmission
				)

	if 'year' in request.GET:
		year = request.GET['year']
		if year:
			cars = cars.filter(

				year__iexact=year

				) 

	if 'body_style' in request.GET:
		body_style = request.GET['body_style']
		if body_style:
			cars = cars.filter(

				body_style__iexact=body_style
				)


	if 'min_price' in request.GET:
		min_price = request.GET['min_price']
		max_price = request.GET['max_price']
		if max_price:
			cars = cars.filter(

				price__gte=min_price,
				price__lte=max_price

				)

	if 'transmission' in request.GET:
		transmission = request.GET['transmission']
		if transmission:
			cars = cars.filter(

				transmission__iexact=transmission

				)
	cars_count = cars.count()
	template_name = 'page/search.html'
	context = {

		'cars' : cars,
		'cars_count' : cars_count,
		'model_search':model_search,
		'city_search':city_search,
		'body_style_search':body_style_search,
		'year_search':year_search,
		'transmission_search': transmission_search,

	}

	return render(request, template_name, context)

def contact(request):

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		phone = request.POST['phone']
		message = request.POST['message']

		current_site = get_current_site(request)
		email_subject = "Vous avez reçu un message du site " + str(current_site) 
		message_body ='Sujet: ' + subject + '\nNom: ' + name + '\nAdresse email: ' + email + '\nTelephone: ' + phone + '\nMessage: ' + message
		admin = Account.objects.get(is_superadmin=True)
		admin_email = admin.email
		send_mail(
		    email_subject,
		    message_body,
		    'De ' + email,
		    [admin_email],
		    fail_silently=False,
		)

		messages.success(request, "Merci de nous avoir contacté.\nNotre équipe vous contactera dans un bref délai.")
		return redirect('contact')

	return render(request, 'page/contact.html', {})