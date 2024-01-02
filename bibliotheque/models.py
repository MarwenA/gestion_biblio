from django.db import models

class Auteur(models.Model):
    code_auteur = models.AutoField(primary_key=True)
    nom_auteur = models.CharField(max_length=100)
    prenom_auteur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom_auteur}, {self.prenom_auteur}"

class Livre(models.Model):
    code_livre = models.AutoField(primary_key=True)
    titre_livre = models.CharField(max_length=100)
    nbre_pages = models.IntegerField()
    exemplaires_disponibles = models.IntegerField(default=0)
    code_auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre_livre

class Adherent(models.Model):
    code_adh = models.AutoField(primary_key=True)
    nom_adh = models.CharField(max_length=100)
    nbr_emprunts_adh = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_adh

class Emprunt(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour_prevue = models.DateField()

    def __str__(self):
        return f"{self.adherent.nom_adh} emprunte {self.livre.titre_livre}"

    