#!/usr/bin/env python
from netmiko import ConnectHandler

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
}

net_connect = ConnectHandler(**nxos1)

print(net_connect.find_prompt())

