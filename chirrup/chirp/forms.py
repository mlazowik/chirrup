from django import forms
from django.contrib.auth.models import User


class ChirpForm(forms.Form):
    text = forms.CharField(
        label='Text',
        widget=forms.Textarea(attrs={'placeholder': "What's up?"}),
        max_length=140
    )
