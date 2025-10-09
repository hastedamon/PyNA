import os
import yaml
from netmiko import ConnectHandler

netmiko_yaml = "/home/david/.netmiko.yml"

with open(netmiko_yaml) as f:
    inventory = yaml.safe_load(f)

cisco3 = inventory["cisco3"]
net_connect = ConnectHandler(**cisco3)

print(net_connect.find_prompt())

net_connect.disconnect()
