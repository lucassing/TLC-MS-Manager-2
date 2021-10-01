import serial.tools.list_ports as list_ports


def connected_devices_name():
    ports = list_ports.comports(include_links=True)
    names = set(map(lambda x: x.name, ports))
    return names
