# Generated by Django 3.0.5 on 2020-05-01 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0002_auto_20200430_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convocatorias', to=settings.AUTH_USER_MODEL, verbose_name='empresa'),
        ),
    ]