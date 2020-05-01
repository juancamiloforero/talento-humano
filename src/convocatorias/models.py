from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from .managers import CustomUserManager
from .validators import FileValidator
import datetime

class User(AbstractUser):
    email = models.EmailField(_('email'), unique=True)
    is_company = models.BooleanField(_('es empresa'), default=False)
    is_candidate = models.BooleanField(_('es candidato'), default=True)
    is_active = models.BooleanField(_('está activo'), default=True)
    is_admin = models.BooleanField(_('es admin'), default=False)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    now = datetime.datetime.now()
    return 'curriculums/{0}-{1}-{2}'.format(instance.name, now, filename)

class Anonymous(models.Model):
    name = models.CharField(_('nombre completo'), max_length=120, validators=[MinLengthValidator(5)])
    curriculum = models.FileField(_('curriculo'), upload_to=user_directory_path, validators=[FileValidator(max_size=10*1024*1024, allowed_extensions='pdf')])

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
    created_at = models.DateTimeField(_('fecha y hora de registro'), auto_now_add=True)
    updated_at = models.DateTimeField(_('fecha y hora de última actualización'), auto_now=True)
