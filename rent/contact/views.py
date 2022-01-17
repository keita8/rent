from .models import Contact, About
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from accounts.models import Account


# Create your views here.

def inquiry(request):

	if request.method == 'POST':
		car_id = request.POST['car_id']
		car_title = request.POST['car_title']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		city = request.POST['city']
		state = request.POST['state']
		customer_need = request.POST['customer_need']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']

		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
			if has_contacted:
				message = "Vous avez deja soumis une requête à propos de cette voiture, notre équipe va vous contacter dans un bref délai."
				messages.error(request, message)
				return redirect('/car/'+car_id)
		else:
			pass


		contact = Contact(city=city, area=state,car_id=car_id, first_name=first_name, last_name=last_name,customer_need=customer_need,email=email,phone=phone,message=message,user_id=user_id,car_title=car_title,)

		admin = Account.objects.get(is_superadmin=True)
		admin_email = admin.email
		send_mail(
		    'Keita location nouvelle requête',
		    'Vous avez reçu une demande à propos de la voiture ' + car_title + ' veuillez traiter cette demande.' ,
		    'De ' + email,
		    [admin_email],
		    fail_silently=False,
		)



		contact.save()
		messages.success(request, 'Votre rêquete a bien été soumise, notre équipe vous contactera le plus tôt que possible.')
		return redirect('/car/'+car_id)


def about(request):

	apropos = About.objects.first()

	context = {
		'about' : apropos
	}
	
	return render(request, 'page/about.html', context)
