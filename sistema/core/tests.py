from django.test import TestCase

# Create your tests here.


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
        
        
    def test_get(self):
        '''get / precisa retornar status 200'''
        self.assertEqual( 200, self.response.status_code)
        
        
    def test_template(self):
        ''' Precisa usar o index.html'''
        self.assertTemplateUsed(self.response, 'index.html')