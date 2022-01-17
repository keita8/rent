from django.db import models

# Create your models here.
class Social(models.Model):
    facebook_link = models.URLField(verbose_name='Lien Facebook')
    twitter_link = models.URLField(verbose_name='Lien Twitter')
    instagram_link = models.URLField(verbose_name='Lien Instagram')
    linkedin_link = models.URLField(verbose_name='Lien linkedin')

    class Meta:
        verbose_name_plural = 'Liens de medias sociaux'

    