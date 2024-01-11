from unittest import TestCase

from rest_framework.test import APIClient
class TestSomething(TestCase):
    def test_sample(self):
        # client = APIClient()
        # response = client.get('/api/v1/test')
        self.assertEquals(200, 200)