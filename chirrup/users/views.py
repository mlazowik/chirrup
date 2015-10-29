from django.views.generic.edit import CreateView

from forms import RegistrationForm


class RegisterUser(CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = '/'
