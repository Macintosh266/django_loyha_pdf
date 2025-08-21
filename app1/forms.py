from django import forms
from .models import *

class CarsForm(forms.ModelForm):
    class Meta:
        model=Cars
        fields = ['title', 'context', 'carmodel',  'is_bool']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control'}),
            'carmodel': forms.Select(attrs={'class': 'form-control'}),
            'is_bool': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CarModelForm(forms.ModelForm):
    class Meta:
        model=CarModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SearchForm(forms.Form):
    word = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search...'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

