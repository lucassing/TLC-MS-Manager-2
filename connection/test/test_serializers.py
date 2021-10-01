from django.test import TestCase
from connection.serializer import PortsConnectedSerializer


class PortsConnectedSerializerTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_list(self):
        serializer = PortsConnectedSerializer()

    def test_no_connected(self):
        serializer = PortsConnectedSerializer()

