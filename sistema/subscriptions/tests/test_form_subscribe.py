from django.test import TestCase
from sistema.subscriptions.forms import SubscriptionForm

class TestSubscriptionFormTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
        self.form = self.response.context['form']
        
    def test_has_form(self):
        '''O contexto precisa do form de subscrição'''
        self.assertIsInstance(self.form, SubscriptionForm)
        
    def test_form_has_fields(self):
        '''Form precisa conter 4 canmpos'''
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields))