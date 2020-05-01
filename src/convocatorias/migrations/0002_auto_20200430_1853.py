# Generated by Django 3.0.5 on 2020-04-30 23:53

import convocatorias.models
import convocatorias.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymous',
            name='curriculum',
            field=models.FileField(upload_to=convocatorias.models.user_directory_path, validators=[convocatorias.validators.FileValidator(allowed_extensions='pdf', max_size=10485760)], verbose_name='curriculo'),
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='name',
            field=models.CharField(max_length=120, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='nombre completo'),
        ),
    ]
