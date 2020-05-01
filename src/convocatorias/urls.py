from django.urls import path
from .views import AllConvocatoriasView, AplicarConvocatoriaView, AplicarConvocatoriaAnonimoView, ListaMisConvocatoriasView

urlpatterns = [
    path('', AllConvocatoriasView.as_view(), name='convocatorias.all_convocatorias'),
    path('aplicar/<int:pk>', AplicarConvocatoriaView.as_view(), name='convocatorias.aplicar'),
    path('aplicar/anonimo/<int:pk>', AplicarConvocatoriaAnonimoView.as_view(), name='convocatorias.aplicar_anonimo'),

    path('aspirante', ListaMisConvocatoriasView.as_view(), name='convocatorias.aspirante.mis_convocatorias')
]