from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.urls import reverse
# from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from tinymce.models import HTMLField

class Car(models.Model):

    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    features_choices = (
        ('Contrôle de vitesse', 'Contrôle de vitesse'),
        ('Interface audio', 'Interface audio'),
        ('Airbags', 'Airbags'),
        ('Air Conditionné', 'Air Conditionné'),
        ('Chauffage des sièges', 'Chauffage des sièges'),
        ('Systeme d\'alarme', 'Systeme d\'alarme'),
        ('Systeme de parking', 'Systeme de parking'),
        ('Direction assistée', 'Direction assistée'),
        ('Camera de recul', 'Camera de recul'),
        ('Injection de caburant', 'Injection de caburant'),
        ('Auto demarrage/arrêt', 'Auto demarrage/arrêt'),
        ('Deflecteur', 'Deflecteur'),
        ('Assistant Bluetooth', 'Assistant Bluetooth'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    color_choice = (
        ('Azur clair', 'Azur clair'),
        ('Bleu clair','Bleu clair'),
        ('Bleu charron','Bleu charron'),
        ('Bleu sarcelle','Bleu sarcelle'),
        ('Bleu canard','Bleu canard'),
        ('Bleu fumée','Bleu fumée'),
        ('Lavande','Lavande'),
        ('Givré', 'Givré'),
        ('Pastel', 'Pastel'),
        ('Cerise', 'Cerise'),
        ('Lie de vin', 'Lie de vin'),
        ('Indigo', 'Indigo'),
        ('Pourpre', 'Pourpre'),
        ('Prune', 'Prune'),
        ('Violet', 'Violet'),
        ('Rouge-violet', 'Rouge-violet'),
        ('Magnata foncé', 'Magnata foncé'),
        ('Aubergine', 'Aubergine'),
        ('Pêche', 'Pêche'),
        ('Rose thé', 'Rose thé'),
        ('Framboise', 'Framboise'),
        ('Rose', 'Rose'),
        ('Saumon', 'Saumon'),
        ('Cerise', 'Cerise'),
        ('Mauve', 'Mauve'),
        ('Framboise', 'Framboise'),
        ('Bisque', 'Bisque'),
        ('Rouge bordeaux', 'Rouge bordeaux'),
        ('Rouge corail', 'Rouge corail'),
        ('Rouge granat', 'Rouge granat'),
        ('Rouge bismark', 'Rouge bismark'),
        ('Rouge alizarine', 'Rouge alizarine'),
        ('Rouge bourgogne', 'Rouge bourgogne'),
        ('Rouge vif', 'Rouge vif'),
        ('Rouge cerise', 'Rouge cerise'),
        ('Aurore', 'Aurore'),
        ('Carotte', 'Carotte'),
        ('Citrouille', 'Citrouille'),
        ('Melon', 'Melon'),
        ('Orange brûlée', 'Orange brûlée'),
        ('Mandarine', 'Mandarine'),
        ('Safran', 'Safran'),
        ('Vanille', 'Vanille'),
        ('Orangé', 'Orangé'),
        ('Ambre', 'Ambre'),
        ('Blond', 'Blond'),
        ('Citron', 'Citron'),
        ('Fauve', 'Fauve'),
        ('Or', 'Or'),
        ('Orpiment', 'Orpiment'),
        ('Soufre', 'Soufre'),
        ('Orc jaune', 'Orc jaune'),
        ('Asperge', 'Asperge'),
        ('Bleu sarcelle', 'Bleu sarcelle'),
        ('Bleu canard', 'Bleu canard'),
        ('Vert épinard', 'Vert épinard'),
        ('Vert olive', 'Vert olive'),
        ('Vert sapin', 'Vert sapin'),
        ('Vert kaki', 'Vert kaki'),
        ('Vert militaire', 'Vert militaire'),
        ('Vert pomme', 'Vert pomme'),
        ('Vert veronese', 'Vert veronese'),
        ('Vert pin', 'Vert pin'),
        ('Brou de noix', 'Brou de noix'),
        ('Noir charbon', 'Noir charbon'),
        ('Ebène', 'Ebène'),
        ('Noir d\'encre', 'Noir d\'encre'),
        ('Dorian', 'Dorian'),
        ('Noiraud', 'Noiraud'),
        ('Cassis', 'Cassis'),
        ('Brun', 'Brun'),
        ('Acajou', 'Acajou'),
        ('Alezan', 'Alezan'),
        ('Auburn', 'Auburn'),
        ('Beige', 'Beige'),
        ('Beige clair', 'Beige clair'),
        ('Beigeasse', 'Beigeasse'),
        ('Bronze', 'Bronze'),
        ('Châtin', 'Châtin'),
        ('Chaudron', 'Chaudron'),
        ('Sang de boeuf', 'Sang de boeuf'),
        ('Marron', 'Marron'),
        ('Caramelle', 'Caramelle'),
        ('Basané', 'Basané'),
        ('Gris', 'Gris'),
        ('Ardoise', 'Ardoise'),
        ('Argent', 'Argent'),
        ('Celadon', 'Celadon'),
        ('Bitume', 'Bitume'),
        ('Gris perle', 'Gris perle'),
        ('Etain pur', 'Etain pur'),
        ('Tourdille', 'Tourdille'),
        ('Gris souris', 'Gris souris'),
        ('Albâtre', 'Albâtre'),
        ('Azur brume', 'Azur brume'),
        ('Blanc de lait', 'Blanc de lait'),
        ('Blanche', 'Blanche'),
        ('Blanc crème', 'Blanc crème'),
        ('Blanc neige', 'Blanc neige'),
        )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    type_choice = (
        ('Berline', 'Berline'),
        ('Coupé', 'Coupé'),
        ('Hayon', 'Hayon'),
        ('Break', 'Break'),
        ('Limousine', 'Limousine'),
        ('Pick Up', 'Pick Up'),
        ('Crossovers', 'Crossovers'),
        ('SUV', 'SUV'),
        ('Fourgonnette', 'Fourgonnette'),
        ('Minivan', 'Minivan'),
        ('Liftback', 'Liftback'),
        ('Cabriolet', 'Cabriolet'),
        ('Minibus', 'Minibus'),
        ('Roadsters', 'Roadsters'),
        ('Targa', 'Targa'),
        ('4X4', '4X4'),
        ('Monospace', 'Monospace'),

        )

    gearbox_choice = (
        ('Manuelle', 'Manuelle'),
        ('Automatique', 'Automatique'),
        )

    fuel_type = (

        ('Essence', 'Essence'),
        ('Diesel', 'Diesel'),
        ('Electrique', 'Electrique')
        )

    condition_choices = ( ('Occasion', 'Occasion'), ('Neuve', 'Neuve') )


    car_title    = models.CharField(max_length=200, verbose_name='Nom de la voiture')
    slug         = models.SlugField(max_length=200, unique=True)
    state        = models.CharField(choices=state_choice,max_length=200, verbose_name='Etat')
    city         = models.CharField(max_length=200, verbose_name='Ville')
    color        = models.CharField(choices=color_choice, max_length=200, verbose_name='Couleur Exterieure')
    modele       = models.CharField(max_length=200, verbose_name='Modèle')
    year         = models.IntegerField(('Année'), choices=year_choice)
    condition    = models.CharField(max_length=200, verbose_name='Condition', choices=condition_choices)
    price        = 	models.PositiveIntegerField( verbose_name='Prix')
    description  = HTMLField(verbose_name='Description')
    features     = MultiSelectField(choices=features_choices, verbose_name='Fonctionnalités', max_length=5000)
    body_style   = models.CharField(choices=type_choice,max_length=200,verbose_name='Type de Vehicule')
    engine       = models.CharField(max_length=200, verbose_name='Moteur')
    transmission = models.CharField(max_length=200)
    gearbox      = models.CharField(choices=gearbox_choice, max_length=200, verbose_name='Boîte de vitesse', default='Manuelle')
    interior     = models.CharField(max_length=200, verbose_name='Decoration interieure')
    milage       = models.IntegerField(verbose_name='Kilometrage')
    miles        = models.IntegerField(verbose_name='Km')
    doors        = models.CharField(choices=door_choices,max_length=2,verbose_name='Portière')
    passengers   = models.IntegerField(verbose_name='Passagers')
    vin_no       = models.CharField(max_length=200, verbose_name='Immatriculation', default='N/A')
    fuel         = models.CharField(max_length=200, verbose_name='Carburant', choices=fuel_type)
    is_featured  = models.BooleanField(default=False,verbose_name='Voiture vedette')
    photo        = models.ImageField(upload_to='photo/%Y/%m/%d/')
    image1       = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    image2       = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    image3       = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    image4       = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    for_sale     = models.BooleanField(default=False, verbose_name='A vendre ?')
    no_of_owners = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=datetime.now, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.car_title)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('car:car_detail', args=[self.slug])

    class Meta:
        verbose_name = 'Vehicule'
        verbose_name_plural = 'Vehicules'



class Banner(models.Model):
    title = HTMLField(verbose_name="Titre")
    content = HTMLField(verbose_name="Contenu")
    image = models.ImageField(upload_to="media/banniere")

    class Meta:
        verbose_name = "Bannière"
        
