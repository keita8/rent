from django.db import models

# Create your models here.
class Team(models.Model):
	
	first_name    = models.CharField(max_length=200, verbose_name='Nom')
	last_name     = models.CharField(max_length=200, verbose_name='Prenom')
	designation   = models.CharField(max_length=200, verbose_name='Fonction')
	photo         = models.ImageField(upload_to='photo/%Y/%m/%d/')
	facebook_link = models.URLField(max_length=200, verbose_name='Lien Facebook')
	twitter_link  = models.URLField(max_length=200, verbose_name='Lien Twitter')
	google_link   = models.URLField(max_length=200,verbose_name='Lien Google')
	created_date  = models.DateTimeField(auto_now_add=True, verbose_name='Date d\'ajout')
	


	class Meta:
		verbose_name = "Equipe Technique"
		verbose_name_plural = "Equipes Techniques"


	def __str__(self):
		return f"{self.first_name} - {self.designation}"

