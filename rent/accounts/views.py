from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators  import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from accounts.forms import UserForm
import requests

# Connexion
def login(request):

    form = UserForm()

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(email=email, password=password)
        
            if user is not None:
                auth.login(request, user)
                # messages.success(request, 'Nous sommes ravis de vous revoir.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Votre adresse email ou votre mot de passe est incorrecte')
                return render(request, 'accounts/login.html')
    else:
        form = UserForm()

    context = {
     'form' : form,
    }
    
    return render(request, 'accounts/login.html', context) 


# Déconnexion
@login_required(login_url = 'login')
def logout_user(request):
	auth.logout(request)
	messages.success(request, 'Vous êtes deconnecté.')
	return redirect('login')

# Inscription
def register(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():

                email        = form.cleaned_data['email']
                password     = form.cleaned_data['password']
                username     = email.split('@')[0]
                user = Account.objects.create_user(email=email, username=username, password=password)
                # user.phone = phone
                user.save()

                # LIEN D'ACTIVATION DU COMPTE
                current_site = get_current_site(request)
                mail_subject = "Lien d'activation de votre compte"
                message      = render_to_string('accounts/account_verification_email.html', {
                    'user'   : user,
                    'domain' : current_site,
                    'uid'    : urlsafe_base64_encode(force_bytes(user.pk)),
                    'token'  : default_token_generator.make_token(user),
                    } )
                to_email=email
                send_email=EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()
                # messages.success(request, "Compte crée avec succès")
                # return redirect('accounts:login')
                return redirect('/accounts/login/?command=verification&email='+email)

        else:
            form = RegistrationForm()

        context = {
        'form' : form,
        }
        return render(request, 'accounts/register.html', context)

# Lien d'activation du compte
def activate(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Votre compte a bien été activé')
        return redirect('login')
    else:
        messages.error(request, 'Ce lien d\'activation a deja expiré.')
        return redirect('register')


# Dashboard
@login_required(login_url='login')
def dashboard(request):

    template_name = 'accounts/dashboard.html'
    context = {}

    
    return render(request, template_name, context)


# Réinitialiser le mot de passe
def forgot_password(request):

    if request.method == "POST":
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # LIEN D'ACTIVATION DU COMPTE
            current_site = get_current_site(request)
            mail_subject = "Réinitialisation de votre mot de passe"
            message      = render_to_string('accounts/reset_password_email.html', {
                'user'   : user,
                'domain' : current_site,
                'uid'    : urlsafe_base64_encode(force_bytes(user.pk)),
                'token'  : default_token_generator.make_token(user),
                } )
            to_email=email
            send_email=EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Un lien de réinitialisation de votre mot de passe vous a été envoyé ')
            return redirect('login')

        else:
            messages.error(request, 'Cette adresse email n\'est associée à aucun compte.')
            return redirect('forgot_password')


    template_name = 'accounts/forgot_password.html'
    context = {}
    
    return render(request, template_name, context)

def reset_password_validate(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'Entrez votre nouveau mot de passe')
        return redirect('reset_password')
    else:
        messages.error(request, 'Ce lien a déjà expiré')
        return redirect('forgot_password')

def reset_password(request):

    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Votre mot de passe a été changé avec succès.')
            return redirect('login')

        else:
            messages.error(request, 'Les mots de passe ne sont pas identiques.')
            return redirect('reset_password')
    else:
        template_name = 'accounts/reset.html'
        context = {}
        
        return render(request, template_name, context)



