import os
import time
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
    }

net_connect = ConnectHandler(**device)

# a)
print("Command prompt:")
print(net_connect.find_prompt())
print()

# b)
print("Config prompt:")
net_connect.config_mode()
print(net_connect.find_prompt())
print()

# c)
print("Exit config prompt:")
net_connect.exit_config_mode()
print(net_connect.find_prompt())
print()

# d)
print("Write Channel '''Disable'''")
net_connect.write_channel("disable\n")
# print(net_connect.find_prompt())
# print()

# e)
time.sleep(2)
print(net_connect.read_channel())
print()

# f)
print("Enable and find prompt:")
net_connect.enable()
print(net_connect.find_prompt())
print()


net_connect.disconnect()
