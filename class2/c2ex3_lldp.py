#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**cisco4)

command = "show lldp neighbors detail"
output = net_connect.send_command(command, use_textfsm=True)
remote_int = output[0]['neighbor_interface']

net_connect.disconnect()

print("##################")
print(f"Neighbor Interface :",remote_int)
print("##################")

