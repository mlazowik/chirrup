from django.conf import settings
from django.shortcuts import render
from chirp.models import Chirp


def index(request):
    if request.user.is_authenticated():
        context = {'chirps': Chirp.objects.all()[:settings.CHIRPS_PER_PAGE]}
        return render(request, 'webview/index-user.html', context)
    else:
        return render(request, 'webview/index-anon.html')