from django.shortcuts import render
from django.views import View
from convocatorias.models import User

class MisConvocatoriasView(View):
    def get(self, request):
        mis_conv = User.objects.get(id=request.user.id).candidates.all()

        context = {
            'convocatorias': mis_conv,
        }
        return render(request, 'aspirante/mis_convocatorias.html', context=context)
