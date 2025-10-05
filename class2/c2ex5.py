import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

devices = [{
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
#    "fast_cli" : True,
    },
    {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
#    "fast_cli" : True,
    }]


for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file("ex5config.txt")
    net_connect.save_config()
    print()
    print(net_connect.find_prompt())
    print(output) 
    print()

net_connect.disconnect()
