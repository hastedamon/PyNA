import json
from pprint import pprint

filename = "arista_arp.json"
with open(filename) as f:
    my_data = json.load(f)

print("-" * 10)
pprint(my_data)
print("-" * 10)

ip_macs = {}

for k, v in my_data.items():
    if k == "ipV4Neighbors":
        for neig_intf in my_data[k]:
            ip_macs[neig_intf["address"]]=neig_intf["hwAddress"]

print()
print(ip_macs)
print()
