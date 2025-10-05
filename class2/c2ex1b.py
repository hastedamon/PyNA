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
output = net_connect.send_command(command, expect_string=r'ip', strip_prompt=False, strip_command=False)
output += net_connect.send_command("", expect_string=r'address', strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8", expect_string=r'count', strip_prompt=False, strip_command=False)
output += net_connect.send_command("", expect_string=r'size', strip_prompt=False, strip_command=False)
output += net_connect.send_command("", expect_string=r'seconds', strip_prompt=False, strip_command=False)
output += net_connect.send_command("", expect_string=r'commands', strip_prompt=False, strip_command=False)
output += net_connect.send_command("", expect_string=r'sizes', strip_prompt=False, strip_command=False)
output += net_connect.send_command("", expect_string=r'ms', strip_prompt=False, strip_command=False)

net_connect.disconnect()

print()
print(output)
print()
