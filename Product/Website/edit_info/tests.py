from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .views import *

class Test_login_view(TestCase):
    def test_login_response(self):
        request = self.client.get(reverse('login'))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, login)


class Test_edit_hub_view(TestCase):
    def test_edithub_redirect(self):
        request = self.client.get(reverse("edit_hub"))
        self.assertRedirects(request, "/accounts/login/?next=/edit/profile/")

    def test_edithub_login(self):
        #simulate user login
        user = User.objects.create_user(username="Mock", password="secret")
        counselor = Counselor.objects.create(name="Mock", accountId=user.id)
        project = Project.objects.create(title="Mock")
        counselor.projects.add(project)
        self.client.login(username="Mock", password="secret")

        request = self.client.get(reverse("edit_hub"))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, edit_hub)


class Test_create_project_view(TestCase):
    def test_create_project_redirect(self):
        request = self.client.get(reverse("create_project"))
        self.assertRedirects(request, "/accounts/login/?next=/edit/profile/create/")

    def test_create_project_login(self):
        #simulate user login using Mock
        user = User.objects.create_user(username="Mock", password="secret")
        counselor = Counselor.objects.create(name="Mock", accountId=user.id)
        project = Project.objects.create(title="Mock")
        counselor.projects.add(project)
        self.client.login(username="Mock", password="secret")

        request = self.client.get(reverse("create_project"))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, create)

class Test_edit_project_view(TestCase):
    def test_edit_project_redirect(self):
        request = self.client.get(reverse("edit_project" , args=(1,)))
        self.assertRedirects(request, "/accounts/login/?next=/edit/project/edit/1")

    def test_edit_project_login(self):
        #simulate user login using Mocks
        user = User.objects.create_user(username="Mock", password="secret")
        counselor = Counselor.objects.create(name="Mock", accountId=user.id)
        project = Project.objects.create(title="Mock")
        counselor.projects.add(project)
        self.client.login(username="Mock", password="secret")

        request = self.client.get(reverse("edit_project", args=(user.id,)))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, edit_project)

class Test_logout_view(TestCase):
    def test_logout_redirect(self):
        #simulate user login, using Mock
        User.objects.create_user(username="Mock", password="secret")
        self.client.login(username="Mock", password="secret")

        request = self.client.get(reverse('logout'))
        self.assertTrue(request.status_code == 302)
        self.assertEquals(request.resolver_match.func, logout)
        self.assertRedirects(request, reverse("index"))

class Test_auth_login(TestCase):
    def test_login_response(self):
        #simulate user login using Mocks
        user = User.objects.create_user(username="Mock", password="secret")
        counselor = Counselor.objects.create(name="Mock", accountId=user.id)
        project = Project.objects.create(title="Mock")
        counselor.projects.add(project)
        self.client.login(username="Mock", password="secret")

        request = self.client.post(reverse("auth_login"), {"username": "Mock", "password": "secret"})
        self.assertRedirects(request, reverse("edit_hub"))
        self.assertTrue(request.status_code == 302)

    def test_badlogin_response(self):
        request = self.client.post(reverse("auth_login"), {"username": "Mock", "password": "notCorrect"})
        self.assertTrue(request.status_code == 200)
        self.assertTrue(request.context["bad_login"])
