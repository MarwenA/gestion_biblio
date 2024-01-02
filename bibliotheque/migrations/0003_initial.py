# Generated by Django 4.2 on 2024-01-02 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bibliotheque', '0002_remove_emprunt_adherent_remove_emprunt_livre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adherent',
            fields=[
                ('code_adh', models.AutoField(primary_key=True, serialize=False)),
                ('nom_adh', models.CharField(max_length=100)),
                ('nbr_emprunts_adh', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('code_auteur', models.AutoField(primary_key=True, serialize=False)),
                ('nom_auteur', models.CharField(max_length=100)),
                ('prenom_auteur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('code_livre', models.AutoField(primary_key=True, serialize=False)),
                ('titre_livre', models.CharField(max_length=100)),
                ('nbre_pages', models.IntegerField()),
                ('exemplaires_disponibles', models.IntegerField(default=0)),
                ('code_auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.auteur')),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(auto_now_add=True)),
                ('date_retour_prevue', models.DateField()),
                ('adherent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.adherent')),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.livre')),
            ],
        ),
    ]
