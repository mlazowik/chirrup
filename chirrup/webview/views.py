from django.shortcuts import render
from chirp.models import Chirp


def index(request):
    context = {'chirps': Chirp.objects.all()[:20]}
    return render(request, 'webview/index.html', context)
