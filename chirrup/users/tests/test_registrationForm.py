from unittest import TestCase
from users.forms import RegistrationForm


class TestRegistrationForm(TestCase):
    def setUp(self):
        self.data = {'username': 'test', 'email': 'u@u.com', 'password1': 'p', 'password2': 'p'}

    def test_email_is_saved(self):
        form = RegistrationForm(data=self.data)
        self.assertTrue(form.is_valid())

        user = form.save()

        self.assertEqual(user.email, 'u@u.com')

    def test_invalid_email_is_rejected(self):
        self.data['email'] = 'u@u.u'
        form = RegistrationForm(data=self.data)

        self.assertFalse(form.is_valid())

    def test_not_matching_passwords_are_rejected(self):
        self.data['password1'] = 'pp'
        form = RegistrationForm(data=self.data)

        self.assertFalse(form.is_valid())
