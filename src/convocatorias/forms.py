from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Convocatoria, Anonymous
from django.utils import timezone

def clean_date(fecha):
    if fecha < timezone.now():
        raise forms.ValidationError("The date cannot be in the past!")
    return fecha

class ConvocatoriaModelForm(forms.ModelForm):
    closing_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'placeholder': 'DD/MM/YYYY HH:MM'
        }),
        label='Fecha y hora de cierre',
        validators=[clean_date]
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