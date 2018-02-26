from django.urls import reverse, resolve
from django.test import TestCase
from .views import home
from .models import TaskItem


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_csrf_exists(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_home_view_resolve_root(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_new_task_post(self):
        url = reverse('home')
        data = {
            'description': 'Example task'
        }
        self.client.post(url, data)
        self.assertTrue(TaskItem.objects.exists())
