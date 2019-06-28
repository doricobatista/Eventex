from django.test import TestCase
from sistema.subscriptions.forms import SubscriptionForm
class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
        self.form = self.response.context['form']
        
    def test_get(self):
        '''Get /inscricao/ precisa retornar statuscode = 200 '''
        self.assertEqual(200, self.response.status_code)
    
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscriptions_form.html')
        
    
    def test_html(self):
        ''' Html precisa conter tags '''
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')
    
    def test_csrf(self):
        '''Html precisa conter csrf'''
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    
    def test_has_form(self):
        '''O contexto precisa do form de subscrição'''
        self.assertIsInstance(self.form, SubscriptionForm)
        
    def test_form_has_fields(self):
        '''Form precisa conter 4 canmpos'''
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields))