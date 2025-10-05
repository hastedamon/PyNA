#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass


cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**cisco4)

command = "ping"
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print(output)
