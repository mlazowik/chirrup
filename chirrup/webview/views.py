from django.shortcuts import render
from chirp.models import Chirp


def index(request):
    return render(request, 'webview/index.html')
