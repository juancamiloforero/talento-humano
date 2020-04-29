# Generated by Django 3.0.5 on 2020-04-28 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anonymous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='nombre completo')),
                ('curriculum', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=120, verbose_name='cargo')),
                ('description', models.TextField(max_length=300, verbose_name='descripción')),
                ('closing_time', models.DateTimeField(verbose_name='fecha y hora de cierre')),
                ('state', models.CharField(choices=[('ABIERTA', 'Abierta'), ('CERRADA', 'Cerrada'), ('TERMINADA', 'Terminada')], default='ABIERTA', max_length=9, verbose_name='estado')),
                ('candidates_anonymous', models.ManyToManyField(to='convocatorias.Anonymous', verbose_name='candidatos anonimos')),
                ('candidates_users', models.ManyToManyField(related_name='candidates', to=settings.AUTH_USER_MODEL, verbose_name='candidatos inscritos')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL, verbose_name='empresa')),
            ],
        ),
    ]