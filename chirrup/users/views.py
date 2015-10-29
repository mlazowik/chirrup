from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic.edit import CreateView
from chirp.models import Chirp

from forms import RegistrationForm


class RegisterUser(CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = '/'


def user_page(request, username):
    user = get_user_model().objects.get(username=username)

    context = {'chirps': Chirp.objects.filter(user=user)}
    return render(request, 'users/user.html', context)
