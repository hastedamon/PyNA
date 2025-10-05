import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "fast_cli" : True,
    }

net_connect = ConnectHandler(**device)

print()
cfg = [
    "ip name-server 1.1.1.1", 
    "ip name-server 1.0.0.1", 
    "ip domain-lookup"
    ]
    
output = net_connect.send_config_set(cfg)

print("-" * 80)
print(output)
print("-" * 80)

verify = net_connect.send_command("ping google.com")

print()
print("+" * 80)
print(verify)
print("+" * 80)
print()

net_connect.disconnect()
