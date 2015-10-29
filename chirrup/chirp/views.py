from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from chirp.models import Chirp
from django.utils import timezone

from .forms import ChirpForm


@login_required
def get_chirp(request):
    if request.method == 'POST':
        form = ChirpForm(request.POST)
        if form.is_valid():
            chirp = Chirp(text=form.cleaned_data['text'], user=request.user, added=timezone.now())
            chirp.save()
            return HttpResponseRedirect(request.POST.get('next'))

    return HttpResponseRedirect('/')
