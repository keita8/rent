from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):

	def create_user(self, username, email, password=None):

		if not email:
			raise ValueError('Vous devez fournir une adresse email')
		
		if not username:
			raise ValueError("Le nom d'utilisateur est requis.")

		user = self.model(

			email = self.normalize_email(email),
			username = username,
			)

		user.set_password(password)
		user.save(using=self._db)


		return user


	def create_superuser(self, username, email, password):
		user = self.create_user(

			email = self.normalize_email(email),
			username = username,
			password = password,

			)

		user.is_active     = True
		user.is_admin      = True
		user.is_staff      = True
		user.is_superadmin = True

		user.save(using=self._db)

		return user





class Account(AbstractBaseUser):

	username   = models.CharField(max_length=80, unique=True, verbose_name="Nom d'utilisateur")
	email      = models.CharField(max_length=200, unique=True, verbose_name='Email')


	# required
	date_joined   = models.DateTimeField(auto_now_add=True, verbose_name='Compte crée')
	last_login    = models.DateTimeField(auto_now_add=True, verbose_name="Dernière connexion")
	is_admin      = models.BooleanField(default=False, verbose_name="admin ?")
	is_active     = models.BooleanField(default=False,verbose_name="Compte activé ?")
	is_staff      = models.BooleanField(default=False, verbose_name="Membre ?")
	is_superadmin = models.BooleanField(default=False, verbose_name="Super administrateur ?")

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	class Meta:
		verbose_name = 'compte utilisateur'
		verbose_name_plural = 'compte utilisateur'


	def __str__(self):
		return str(self.email)

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, add_label):
		return True