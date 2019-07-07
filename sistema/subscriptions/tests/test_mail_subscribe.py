from django.test import TestCase
from django.core import mail
FORM_DATA = dict(name='Dorico Batista', cpf='12345678910',
                 email='doricobatista@gmail.com', phone='279876543210')

class SubscribePostValid(TestCase):
    def setUp(self):

        self.resp = self.client.post('/inscricao/', FORM_DATA)
        
        self.email = mail.outbox[0]
        
    
    def test_subscription_email_subject(self):
        
        expect = 'Confirmação de inscrição'
        
        self.assertEqual(expect, self.email.subject)
    
    
    def test_subscription_email_from(self):
        expect = 'doricobatista@gmail.com'
        self.assertEqual(expect, self.email.from_email)
        
    def test_subscription_email_to(self):
        expect = ['doricobatista@gmail.com', 'doricobatista@gmail.com', ]
        self.assertEqual(expect, self.email.to)
    
    
    def test_subscription_email_body(self):
        for item in FORM_DATA:
            with self.subTest():
                self.assertIn(FORM_DATA[item], self.email.body)