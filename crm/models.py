from django.db import models

class AdressePostale (models.Model):
    localite = models.CharField(max_length=120)
    rue = models.CharField(max_length=120)
    code_postal = models.PositiveSmallIntegerField()

class Telephone (models.Model):
    TYPES_DE_TELEPHONES = (('M','Mobile'),
                           ('F', 'Fixe'))
    numero_de_telephone = models.CharField(max_length=100)
    type_de_telephone = models.CharField(max_length=1, choices=TYPES_DE_TELEPHONES)

class Personne (models.Model):
    nom_de_famille = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    pere = models.ForeignKey('self', null=True)
    mere = models.ForeignKey('self', null=True)
    partenaires = models.ManyToManyField('Partenaire', null=True)
    enfants = models.ManyToManyField('Enfant', null=True)
    date_de_naissance = models.DateField(null=True)
    date_de_deces = models.DateField(null=True)
    est_paroissien = models.BooleanField(default=False)
    adressePostale = models.ForeignKey(AdressePostale, null=True)
    telephones = models.ManyToManyField(Telephone, null=True)

class Partenaire (models.Model):
    TYPES_DE_RELATION = (('M', 'Mariage'),
                ('V', 'Veuvage'),
                ('D', 'Divorcé'),
                ('C', 'Concubinage'),
                ('S', 'Séparé'))
    partenaire = models.ForeignKey(Personne)
    type_de_relation = models.CharField(max_length=1, choices=TYPES_DE_RELATION)
    date_du_statut = models.DateField(null=True)

class Enfant (models.Model):
    enfant = models.ForeignKey(Personne)
