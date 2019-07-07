from django.test import TestCase
from sistema.subscriptions.forms import SubscriptionForm
from django.core import mail
FORM_DATA = dict(name='Dorico Batista', cpf='12345678910',
                 email='doricobatista@gmail.com', phone='279876543210')

class SubscribeGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
        
    def test_get(self):
        '''Get /inscricao/ precisa retornar statuscode = 200 '''
        self.assertEqual(200, self.response.status_code)
    
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscriptions_form.html')
        
    
    def test_html(self):
        ''' Html precisa conter tags '''
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1),
               )
        
        for text, count in tags:
            with self.subTest(): # subTest serve para acumular excecões encontradas.
                self.assertContains(self.response, text, count)

    
    def test_csrf(self):
        '''Html precisa conter csrf'''
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    
        
class SubscribePostValid(TestCase):
    def setUp(self):

        self.resp = self.client.post('/inscricao/', FORM_DATA)
        
        self.email = mail.outbox[0]
        
    def test_post(self):
        ''' Unm POST válido precisa redirecionar para /inscricao/'''
        self.assertEqual(302, self.resp.status_code)
        
        
    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
        
        
class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})
        self.form = self.resp.context['form']
        
    def test_post(self):
        ''' POST inválido não pode redirecionar '''
        
        self.assertEqual(200, self.resp.status_code)
        
        
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscriptions_form.html')
    
    
    def test_has_form(self):
        
        self.assertIsInstance(self.form, SubscriptionForm)
        
    def test_form_has_errors(self):
        self.assertTrue(self.form.errors)
        
class SubscribeSucessMessage(TestCase):
    def test_message(self):
        response = self.client.post('/inscricao/', FORM_DATA, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')
        