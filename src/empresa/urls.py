from django.urls import path
from .views import EmpresaHomeView, MisConvocatoriasView, CrearConvocatoriaView, DetallesConvocatoriaView

urlpatterns = [
    path('', EmpresaHomeView.as_view(), name='empresa.home'),
    path('mis_convocatorias', MisConvocatoriasView.as_view(), name='empresa.mis_convocatorias'),
    path('crear_convocatoria', CrearConvocatoriaView.as_view(), name='empresa.crear_convocatoria'),
    path('detalles_convocatoria/<int:pk>', DetallesConvocatoriaView.as_view(), name='empresa.detalles_convocatoria')
]
