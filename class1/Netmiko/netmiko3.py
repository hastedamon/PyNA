#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**cisco3)

output = net_connect.send_command("show version")

with open("output.txt", "w") as f:
    f.write(output)

net_connect.disconnect()
