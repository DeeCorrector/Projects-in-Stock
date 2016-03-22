from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
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


class Test_logout_view(TestCase):
    def test_logout_redirect(self):
        #simulate user login
        User.objects.create_user(username="mock", password="secret")
        self.client.login(username="mock", password="secret")
        #test response
        request = self.client.get(reverse('logout'))
        self.assertTrue(request.status_code == 302)
        self.assertEquals(request.resolver_match.func, logout)
        #test redirect
        self.assertRedirects(request, reverse("index"))
