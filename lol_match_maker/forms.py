from django import forms
from .models import Champion


class ChampionForm(forms.Form):
    name = forms.CharField(max_length=120, required=True)
    type = forms.CharField(max_length=120, required=True)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Champion.objects.filter(name=name).exists():
            raise forms.ValidationError('Esse nome de campeão já existe.')
        return name
