from rest_framework import serializers
from utils.ports import connected_devices_name


class PortsConnectedSerializer(serializers.Serializer):
    ports = serializers.SerializerMethodField(method_name=connected_devices_name())

    class Meta:
        fields = ('ports',)

