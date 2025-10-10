from os import path
import yaml
from netmiko import ConnectHandler
from pprint import pprint
from ciscoconfparse import CiscoConfParse

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    inventory = yaml.safe_load(f)

cisco4 = inventory["cisco4"]
net_connect = ConnectHandler(**cisco4)
output = net_connect.send_command('show run')

cisco_obj = CiscoConfParse(output.splitlines(), ignore_blank_lines=False)
intf_w_IP = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

for match in intf_w_IP:
    print("\nInterface Line: ",match.text)
    print("IP Address Line: ",match.children[0].text)
print()
net_connect.disconnect()
