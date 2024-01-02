from django.urls import path

from .views import *

urlpatterns = [
    path('',gestion_liste, name='gestion_liste'),

    path('gestion_adherents/', gestion_adherents, name='gestion_adherents'),
    path('ajouter_adherent/',ajouter_adherent, name='ajouter_adherent'),
    path('modifier_adherent/<int:id>/',modifier_adherent, name='modifier_adherent'),
    path('supprimer_adherent/<int:id>/',supprimer_adherent, name='supprimer_adherent'),
    path('liste_adherents/',liste_adherents, name='liste_adherents'),

    path('gestion_livres/', gestion_livres, name='gestion_livres'),
    path('ajouter_livre/', ajouter_livre, name='ajouter_livre'),
    path('modifier_livre/<int:code_livre>/', modifier_livre, name='modifier_livre'),
    path('supprimer_livre/<int:code_livre>/', supprimer_livre, name='supprimer_livre'),
    path('liste_livres/', liste_livres, name='liste_livres'),


    path('gestion_auteurs/', gestion_auteurs, name='gestion_auteurs'),
    path('ajouter_auteur/', ajouter_auteur, name='ajouter_auteur'),
    path('modifier_auteur/<int:code_auteur>/', modifier_auteur, name='modifier_auteur'),
    path('supprimer_auteur/<int:code_auteur>/', supprimer_auteur, name='supprimer_auteur'),
    path('liste_auteurs/', liste_auteurs, name='liste_auteurs'),

    path('gestion_emprunts/', gestion_emprunts, name='gestion_emprunts'),
    path('emprunter_livre/', emprunter_livre, name='emprunter_livre'),
    path('liste_livres_empruntes/',liste_livres_empruntes, name='liste_livres_empruntes'),
    path('rendre_livre/<int:id>/', rendre_livre, name='rendre_livre'),
    path('liste_emprunteurs_livre/<int:code_livre>/', liste_emprunteurs_livre, name='liste_emprunteurs_livre'),
    path('liste_retardataires/', liste_retardataires, name='liste_retardataires'),
    path('liste_livres_non_retournes/', liste_livres_non_retournes, name='liste_livres_non_retournes'),
    path('liste_tous_livres/', liste_tous_livres, name='liste_tous_livres'),


    path('histogramme_livres_empruntes/', histogramme_livres_empruntes, name='histogramme_livres_empruntes'),


    path('generate_fake_data/', generate_fake_data, name='generate_fake_data'),





]