import json
from pprint import pprint

filename = "nxos_interfaces.json"
with open(filename) as f:
    my_data = json.load(f)

print("-" * 10)
pprint(my_data)
print("-" * 10)

ipv4 = []
ipv6 = []

for intf, ips_dict in my_data.items():
    protocols = my_data[intf]
    for proto, ip_subn in protocols.items():
        if proto == "ipv4":
            the_ips = protocols[proto]
            for ip, prefix in the_ips.items():
                the_subnet = the_ips[ip]
                ipv4.append([ip + "/" + str(the_subnet["prefix_length"])])
        if proto == "ipv6":
            the_ips = protocols[proto]
            for ip, prefix in the_ips.items():
                the_subnet = the_ips[ip]
                ipv6.append([ip + "/" + str(the_subnet["prefix_length"])])

print()
print(ipv4)
print()
print(ipv6)
print()
