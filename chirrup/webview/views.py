from django.shortcuts import render
from chirp.models import Chirp


def index(request):
    if request.user.is_authenticated():
        context = {'chirps': Chirp.objects.all()[:20]}
        return render(request, 'webview/index-user.html', context)
    else:
        return render(request, 'webview/index-anon.html')