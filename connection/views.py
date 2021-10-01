from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from utils.ports import connected_devices_name


class PortsList(ViewSet):

    def list(self, request):
        devices = connected_devices_name()
        return Response({'device_names': devices})

    def create(self, request):
        pass

