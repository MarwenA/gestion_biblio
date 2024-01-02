from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from datetime import datetime, timedelta
from django.db.models import Count


def gestion_liste(request):
    return render(request, 'gestion_liste.html')


#                     Gestion des Adhérents              #

def gestion_adherents(request):
    return render(request, 'adherent/gestion_adherents.html')

def ajouter_adherent(request):
    if request.method == 'POST':
        nom_adh = request.POST['nom_adh']
        nbr_emprunts_adh = request.POST['nbr_emprunts_adh']
        adherent = Adherent(nom_adh=nom_adh, nbr_emprunts_adh=nbr_emprunts_adh)
        adherent.save()
        return redirect('liste_adherents')

    return render(request, 'adherent/ajouter_adherent.html')

def modifier_adherent(request, id):
    adherent = get_object_or_404(Adherent, code_adh=id)

    if request.method == 'POST':
        adherent.nom_adh = request.POST['nom_adh']
        adherent.nbr_emprunts_adh = request.POST['nbr_emprunts_adh']
        adherent.save()
        return redirect('liste_adherents')

    return render(request, 'adherent/modifier_adherent.html', {'adherent': adherent})

def supprimer_adherent(request, id):
    adherent = get_object_or_404(Adherent, code_adh=id)
    adherent.delete()
    return redirect('liste_adherents')

def liste_adherents(request):
    liste_adherents = Adherent.objects.all()
    return render(request, 'adherent/liste_adherents.html', {'liste_adherents': liste_adherents})

#                     Gestion des Livres                   #  

def gestion_livres(request):
    return render(request, 'livre/gestion_livres.html')

def ajouter_livre(request):
    if request.method == 'POST':
        titre_livre = request.POST['titre_livre']
        nbre_pages = request.POST['nbre_pages']
        exemplaires_disponibles = request.POST['exemplaires_disponibles']
        code_auteur = request.POST['code_auteur']

        Livre.objects.create(
            titre_livre=titre_livre,
            nbre_pages=nbre_pages,
            exemplaires_disponibles=exemplaires_disponibles,
            code_auteur_id=code_auteur
        )

        return redirect('liste_livres')

    auteurs = Auteur.objects.all()
    return render(request, 'livre/ajouter_livre.html', {'auteurs': auteurs})

def modifier_livre(request, code_livre):
    livre = get_object_or_404(Livre, code_livre=code_livre)

    if request.method == 'POST':
        livre.titre_livre = request.POST['titre_livre']
        livre.nbre_pages = request.POST['nbre_pages']
        livre.exemplaires_disponibles = request.POST['exemplaires_disponibles']
        livre.code_auteur_id = request.POST['code_auteur']
        livre.save()

        return redirect('liste_livres')
    auteurs = Auteur.objects.all()
    return render(request, 'livre/modifier_livre.html', {'livre': livre,'auteurs': auteurs})

def supprimer_livre(request, code_livre):
    livre = get_object_or_404(Livre, code_livre=code_livre)
    livre.delete()
    return redirect('liste_livres')

def liste_livres(request):
    liste_livres = Livre.objects.order_by('titre_livre')
    return render(request, 'livre/liste_livres.html', {'liste_livres': liste_livres})


#                     Gestion des auteurs                  # 

def gestion_auteurs(request):
    return render(request, 'auteur/gestion_auteurs.html')

def ajouter_auteur(request):
    if request.method == 'POST':
        nom_auteur = request.POST['nom_auteur']
        prenom_auteur = request.POST['prenom_auteur']

        Auteur.objects.create(
            nom_auteur=nom_auteur,
            prenom_auteur=prenom_auteur
        )

        return redirect('liste_auteurs')

    return render(request, 'auteur/ajouter_auteur.html')

def modifier_auteur(request, code_auteur):
    auteur = get_object_or_404(Auteur, code_auteur=code_auteur)

    if request.method == 'POST':
        auteur.nom_auteur = request.POST['nom_auteur']
        auteur.prenom_auteur = request.POST['prenom_auteur']
        auteur.save()

        return redirect('liste_auteurs')

    return render(request, 'auteur/modifier_auteur.html', {'auteur': auteur})


def supprimer_auteur(request, code_auteur):
    auteur = get_object_or_404(Auteur, code_auteur=code_auteur)
    auteur.delete()
    return redirect('liste_auteurs')

def liste_auteurs(request):
    liste_auteurs = Auteur.objects.order_by('nom_auteur', 'prenom_auteur')
    return render(request, 'auteur/liste_auteurs.html', {'liste_auteurs': liste_auteurs})



#                     Gestion des emprunter                  #  



def gestion_emprunts(request):
    return render(request, 'emprunts/gestion_emprunts.html')


def emprunter_livre(request):
    if request.method == 'POST':
        livre_code = request.POST['livre_code']
        adherent_code = request.POST['adherent_code']
        
        livre = get_object_or_404(Livre, code_livre=livre_code)
        adherent = Adherent.objects.get(code_adh=adherent_code)
        
        date_emprunt = datetime.now()
        date_retour_prevue = date_emprunt + timedelta(days=15)

        emprunt = Emprunt.objects.create(
            adherent=adherent,
            livre=livre,
            date_emprunt=date_emprunt,
            date_retour_prevue=date_retour_prevue
        )

        # Mettre à jour le nombre d'emprunts de l'adhérent
        adherent.nbr_emprunts_adh += 1
        adherent.save()

        # Mettre à jour le nombre d'exemplaires disponibles du livre
        livre.exemplaires_disponibles -= 1
        livre.save()

        return redirect('liste_livres_empruntes')

    livres_disponibles = Livre.objects.filter(exemplaires_disponibles__gt=0)
    adherents = Adherent.objects.all()

    return render(request, 'emprunts/emprunter_livre.html', {'livres_disponibles': livres_disponibles, 'adherents': adherents})

def liste_livres_empruntes(request):
    livres_empruntes = Emprunt.objects.all()
    return render(request, 'emprunts/liste_livres_empruntes.html', {'livres_empruntes': livres_empruntes})

def rendre_livre(request, id):
    emprunt = get_object_or_404(Emprunt, id=id)
    emprunt.adherent.nbr_emprunts_adh -= 1
    emprunt.adherent.save()
    emprunt.livre.exemplaires_disponibles += 1
    emprunt.livre.save()
    emprunt.delete()
    return redirect('liste_livres_empruntes')


def liste_emprunteurs_livre(request, code_livre):
    livre = get_object_or_404(Livre, code_livre=code_livre)
    emprunts = Emprunt.objects.filter(livre=livre)
    return render(request, 'emprunts/liste_emprunteurs_livre.html', {'livre': livre, 'emprunts': emprunts})

def liste_retardataires(request):
    date_actuelle = datetime.now().date()
    retardataires = Emprunt.objects.filter(date_retour_prevue__lt=date_actuelle)
    return render(request, 'emprunts/liste_retardataires.html', {'retardataires': retardataires})

def liste_livres_non_retournes(request):
    date_actuelle = datetime.now().date()
    livres_non_retournes = Emprunt.objects.filter(date_retour_prevue__lt=date_actuelle)
    return render(request, 'emprunts/liste_livres_non_retournes.html', {'livres_non_retournes': livres_non_retournes})

def liste_tous_livres(request):
    livres = Livre.objects.all()
    return render(request, 'emprunts/liste_tous_livres.html', {'livres': livres})


def histogramme_livres_empruntes(request):
    livres_empruntes = Emprunt.objects.values('livre').annotate(count=Count('livre')).order_by('-count')[:10]
    livres_labels = [Livre.objects.get(code_livre=livre['livre']).titre_livre for livre in livres_empruntes]
    livres_counts = [livre['count'] for livre in livres_empruntes]
    data = {
        'labels': livres_labels,
        'counts': livres_counts,
    }
    print(data)
    return render(request, 'statistiques/histogramme_livres_empruntes.html', {'data': data})

from faker import Faker
import random
from django.http import HttpResponse
def generate_fake_data(request):
    fake = Faker()

    # Remplir la table Auteur
    for _ in range(10):
        Auteur.objects.create(
            nom_auteur=fake.last_name(),
            prenom_auteur=fake.first_name()
        )

    # Remplir la table Livre avec des exemplaires disponibles
    for _ in range(20):
        auteur = random.choice(Auteur.objects.all())
        Livre.objects.create(
            titre_livre=fake.catch_phrase(),
            nbre_pages=random.randint(50, 500),
            exemplaires_disponibles=random.randint(1, 5),
            code_auteur=auteur
        )

    # Remplir la table Adherent
    for _ in range(15):
        Adherent.objects.create(
            nom_adh=fake.last_name(),
            nbr_emprunts_adh=random.randint(0, 3)
        )

    # Remplir la table Emprunt avec des emprunts aléatoires
    for _ in range(30):
        adherent = random.choice(Adherent.objects.all())
        livre = random.choice(Livre.objects.filter(exemplaires_disponibles__gt=0))
        Livre.objects.filter(pk=livre.pk).update(exemplaires_disponibles=models.F('exemplaires_disponibles') - 1)
        date_emprunt = fake.date_between(start_date="-30d", end_date="today")
        date_retour_prevue = date_emprunt + timedelta(days=15)
        Emprunt.objects.create(
            adherent=adherent,
            livre=livre,
            date_emprunt=date_emprunt,
            date_retour_prevue=date_retour_prevue
        )
    return HttpResponse("done ")
