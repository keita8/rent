from django.db import models
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.
class Contact(models.Model):
	first_name = models.CharField(max_length=200, verbose_name='Prenom')
	last_name = models.CharField(max_length=200, verbose_name='Nom')
	car_id = models.SlugField(verbose_name='Slug de la voiture')
	car_title = models.CharField(verbose_name='Marque de la voiture')
	customer_need = models.CharField(max_length=200, verbose_name='Besoin du client')
	car_title = models.CharField(max_length=200, verbose_name="Marque de la voiture")
	city = models.CharField(max_length=200, verbose_name="Ville ")
	area = models.CharField(max_length=200, verbose_name='Quartier')
	phone = models.CharField(max_length=20, verbose_name="Téléphone")
	email = models.EmailField(max_length=200)
	message = models.TextField(blank=True)
	user_id = models.IntegerField(blank=True, verbose_name="ID Client")
	created_date = models.DateTimeField(verbose_name="Date d\'envoi", default=datetime.now)

	def __str__(self):
		return f"{self.email}"


class About(models.Model):
	image1 = models.ImageField(upload_to='image/about')
	image2 = models.ImageField(upload_to='image/about')
	image3 = models.ImageField(upload_to='image/about')
	image11 = models.ImageField(upload_to='image/about')
	image22 = models.ImageField(upload_to='image/about')
	image33 = models.ImageField(upload_to='image/about')
	title = HTMLField(verbose_name='Titre')
	description = HTMLField()

	class Meta:
		verbose_name = 'A propos'
	
	def __str__(self):
		return f' {self.title} '