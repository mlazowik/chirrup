from django import forms
from django.contrib.auth.models import User


class ChirpForm(forms.Form):
    text = forms.CharField(label='Text', max_length=140)
