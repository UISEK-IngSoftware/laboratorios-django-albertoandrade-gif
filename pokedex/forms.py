from django import forms
from .models import Pokemon, Trainer


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'type', 'height', 'weight', 'trainer', 'image']
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'height': 'Altura',
            'weight': 'Peso',
            'trainer': 'Entrenador',
            'image': 'Fotografía',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'age', 'city', 'photo']
        labels = {
            'name': 'Nombre',
            'age': 'Edad',
            'city': 'Ciudad',
            'photo': 'Fotografía',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }