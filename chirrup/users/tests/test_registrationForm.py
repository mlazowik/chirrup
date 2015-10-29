from unittest import TestCase
from users.forms import RegistrationForm


class TestRegistrationForm(TestCase):
    def test_email(self):
        data = {'username': 'test', 'email': 'u@u.com', 'password1': 'p', 'password2': 'p'}
        form = RegistrationForm(data=data)

        self.assertTrue(form.is_valid())

        user = form.save()

        self.assertEqual(user.email, 'u@u.com')

