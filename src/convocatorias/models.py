from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Anonymous(models.Model):
    name = models.CharField(_('nombre completo'), max_length=120)
    curriculum = models.FileField(upload_to='documents/')

class Convocatoria(models.Model):
    OPENED = 'ABIERTA'
    CLOSED = 'CERRADA'
    FINISHED = 'TERMINADA'

    ESTADOS_CONVOCATORIA = [
        (OPENED, 'Abierta'),
        (CLOSED, 'Cerrada'),
        (FINISHED, 'Terminada')
    ]

    position = models.CharField(_('cargo'), max_length=120)
    description = models.TextField(_('descripción'), max_length=300)
    closing_time = models.DateTimeField(_('fecha y hora de cierre'))
    state = models.CharField(_('estado'),max_length=9, choices=ESTADOS_CONVOCATORIA, default=OPENED)
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies', verbose_name=_('empresa'))
    candidates_users = models.ManyToManyField(User, related_name='candidates', verbose_name=_('candidatos inscritos'))
    candidates_anonymous = models.ManyToManyField(Anonymous, verbose_name=_('candidatos anonimos'))
