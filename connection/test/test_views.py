from django.test import TestCase
from connection.serializer import PortsConnectedSerializer
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class PortsConnectedViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        pass

    def test_list_con(self):
        url = reverse('connection-list')
        response = self.client.get(url, format='json')
        self.assertEqual()
