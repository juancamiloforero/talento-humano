from django.urls import path
from .views import MisConvocatoriasView

urlpatterns = [
    path('', MisConvocatoriasView.as_view(), name='aspirante.mis_convocatorias')
]