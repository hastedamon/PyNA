import os
import yaml
from netmiko import ConnectHandler

netmiko_yaml = "/home/david/.netmiko.yml"

with open(netmiko_yaml) as f:
    inventory = yaml.safe_load(f)

nxos1 = inventory["nxos1"]
net_connect = ConnectHandler(**nxos1)

print(net_connect.find_prompt())

verify = net_connect.send_command("ping google.com count 3")

print()
print("+" * 80)
print(verify)
print("+" * 80)
print()

net_connect.disconnect()
