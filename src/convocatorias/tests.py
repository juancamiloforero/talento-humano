from django.test import TestCase, RequestFactory
from .models import Convocatoria, User
from .forms import ConvocatoriaModelForm
from django.utils import timezone
import datetime

# Test de formulario ConvocatoriaModelForm
class ConvocatoriaModelFormTestCase(TestCase):
    
    # Probar fecha cierre no puede ser anterior al día de hoy
    def test_fecha_antigua(self):
        date = timezone.now() - datetime.timedelta(seconds=1)
        data = {
            'closing_time': date,
            'position': "Cualquiera",
            'state': "ABIERTA",
            'description': "Cualquiera"
        }
        form = ConvocatoriaModelForm(data=data)
        self.assertFalse(form.is_valid())
    
    # Probar fecha cierre correcto
    def test_fecha_futura(self):
        date = timezone.now() + datetime.timedelta(seconds=1)
        data = {
            'closing_time': date,
            'position': "Cualquiera",
            'state': "ABIERTA",
            'description': "Cualquiera"
        }
        form = ConvocatoriaModelForm(data=data)
        self.assertTrue(form.is_valid())
    ## Por probar mas validaciones