#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**nxos2)

command = "show lldp neighbors detail"
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
net_connect.disconnect()

print(output)
