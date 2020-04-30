from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, CreateView
from .models import Convocatoria, Anonymous
from .forms import AplicarAnonimoForm

def after_login(request):
    if request.user.is_authenticated:
        if request.user.is_company:
            return redirect('empresa/')
        elif request.user.is_candidate:
            return redirect('/')
        else:
            return redirect('logout')

class AllConvocatoriasView(View):
    def get(self, request, **kwargs):
        context = {
            'page_title': "Convocatorias más actuales!",
            'convocatorias': Convocatoria.objects.all().order_by('closing_time')
        }
        print(request)
        # context.update(kwargs['context'])
        return render(request, 'convocatorias/convocatorias.html', context=context)

class AplicarConvocatoriaView(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated and request.user.is_candidate:
            # Buscar la convocatoria seleccionada y asignar al usuario a la convocatoria
            convocatoria = Convocatoria.objects.get(pk=kwargs['pk'])
            context = {
                'page_title': "Convocatorias más actuales!",
                'convocatorias': Convocatoria.objects.all().order_by('closing_time')
            }
            if request.user in convocatoria.candidates_users.all():
                context.update({'estado': "Ya has aplicado a la convocatoria anteriormente!"})    
            else:
                convocatoria.candidates_users.add(request.user)
                context.update({'estado': "Aplicación satisfactoria!"})
            return render(request, 'convocatorias/convocatorias.html', context=context)
        else:
            return redirect('anonimo/' + str(kwargs['pk']))

class AplicarConvocatoriaAnonimoView(CreateView):
    model = Anonymous
    form_class = AplicarAnonimoForm
    template_name = 'convocatorias/aplicar_anonimo.html'
    success_url = '/'

    def form_valid(self, form):
        anonymous = form.save()
        # Buscar la convocatoria y asignar el anónimo a esa convocatoria
        convocatoria = Convocatoria.objects.get(pk=self.kwargs['pk'])
        convocatoria.candidates_anonymous.add(anonymous)
        return super().form_valid(form)
