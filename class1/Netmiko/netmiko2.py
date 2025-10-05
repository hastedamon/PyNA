#!/usr/bin/env python
from netmiko import ConnectHandler

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
}
nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
}

devices = [nxos1,nxos2]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())


# net_connect1 = ConnectHandler(**nxos1)
# net_connect2 = ConnectHandler(**nxos2)


# print(net_connect.find_prompt())

