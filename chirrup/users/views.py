from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.edit import CreateView
from chirp.models import Chirp

from forms import RegistrationForm


class RegisterUser(CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = '/'


@login_required
def users(request):
    context = {'users': get_user_model().objects.all()}
    return render(request, 'users/users.html', context)


@login_required
def user_page(request, username):
    user = get_user_model().objects.get(username=username)

    context = {
        'username': username,
        'chirps': Chirp.objects.filter(user=user)[:settings.CHIRPS_PER_PAGE]
    }

    return render(request, 'users/user.html', context)
