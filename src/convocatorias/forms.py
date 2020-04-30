from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Convocatoria, Anonymous

class ConvocatoriaModelForm(forms.ModelForm):
    closing_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'placeholder': 'DD/MM/YYYY HH:MM'
        }),
        label='Fecha y hora de cierre'
    )

    class Meta:
        model = Convocatoria
        fields = ('position', 'description', 'closing_time', 'state', )

class AplicarAnonimoForm(forms.ModelForm):
    
    class Meta:
        model = Anonymous
        fields = ('name', 'curriculum', )
    
    def save(self, commit=True):
        return super().save(commit=commit)