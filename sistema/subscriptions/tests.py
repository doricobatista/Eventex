from django.core import mail
from django.test import TestCase
from sistema.subscriptions.forms import SubscriptionForm

FORM_DATA = dict(name='Dorico Batista', cpf='12345678910',
                 email='doricobatista@gmail.com', phone='279876543210')

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
        
class SubscribePostTest(TestCase):
    def setUp(self):

        self.resp = self.client.post('/inscricao/', FORM_DATA)
        
        self.email = mail.outbox[0]
        
    def test_post(self):
        ''' Unm POST válido precisa redirecionar para /inscricao/'''
        self.assertEqual(302, self.resp.status_code)
        
        
    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
        
    
    def test_subscription_email_subject(self):
        
        expect = 'Confirmação de inscrição'
        
        self.assertEqual(expect, self.email.subject)
    
    
    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)
        
    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'doricobatista@gmail.com']
        self.assertEqual(expect, self.email.to)
    
    
    def test_subscription_email_body(self):
        for item in FORM_DATA:
            self.assertIn(FORM_DATA[item], self.email.body)
        
        
class SubscribeInvalidPost(TestCase):
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
        
        