from django.shortcuts import render
from convocatorias.models import Convocatoria
from convocatorias.forms import ConvocatoriaModelForm
from django.views import View
from django.views.generic import FormView, DetailView

class MisConvocatoriasView(View):
    def get(self, request):
        context = {
            'convocatorias': Convocatoria.objects.all()
        }
        return render(request, 'empresa/mis_convocatorias.html', context=context)

class EmpresaHomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'empresa/empresa.html', context=context)

class CrearConvocatoriaView(FormView):
    form_class = ConvocatoriaModelForm
    template_name = 'empresa/crear_convocatoria.html'
    success_url = 'mis_convocatorias'

    def form_valid(self, form):
        form.instance.company = self.request.user
        form.save()
        return super().form_valid(form)

class DetallesConvocatoriaView(DetailView):
    model = Convocatoria
    template_name = 'empresa/detalles_convocatoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['candidates'] = Convocatoria.objects.get(id=kwargs['object'].pk).candidates_users.all()
        context['anonymous'] = Convocatoria.objects.get(id=kwargs['object'].pk).candidates_anonymous.all()
        return context
