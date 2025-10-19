from django.test import TestCase
from django.urls import reverse

class BasicViewsTest(TestCase):
    def test_home_get(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
