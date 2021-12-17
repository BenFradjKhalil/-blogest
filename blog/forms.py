from django import forms
from django.forms.widgets import Textarea


class ContactForm(forms.Form):
    nom=forms.CharField(max_length=200)
    prenom=forms.CharField(max_length=200)
    email=forms.EmailField()
    message=forms.CharField(widget=Textarea)