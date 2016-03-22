from django.test import TestCase
from django.core.urlresolvers import reverse
from .views import *

#Views testing
######Reference#######
#class Test_index_view(TestCase):
#    def test_index_response(self):
#        request = self.client.get(reverse('index'))
#        self.assertTrue(request.status_code == 200)
#        self.assertEquals(request.resolver_match.func, index)
######################

class Test_login_view(TestCase):
    def test_login_response(self):
        request = self.client.get(reverse('login'))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, login)
