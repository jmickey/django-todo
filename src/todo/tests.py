from django.urls import reverse, resolve
from django.test import TestCase
from .views import home


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_view_resolve_root(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
