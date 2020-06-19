from django import forms
from .models import Monster, Sighting

class MonsterForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = '__all__'

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'