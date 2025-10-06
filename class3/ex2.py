import yaml
from pprint import pprint

lab_devices = []

device1 = {"cisco3":{"device_name":"cisco3","host":"cisco3.lasthop.io","username":"labuser","password":"userlab01"}}
device2 = {"cisco4":{"device_name":"cisco4","host":"cisco4.lasthop.io","username":"labuser","password":"userlab01"}}
device3 = {"arista1":{"device_name":"arista1","host":"arista1.lasthop.io","username":"labuser","password":"userlab01"}}
device4 = {"arista2":{"device_name":"arista2","host":"arista2.lasthop.io","username":"labuser","password":"userlab01"}}
device5 = {"nxos1":{"device_name":"nxos1","host":"nxos1.lasthop.io","username":"labuser","password":"userlab01"}}

lab_devices.extend([device1,device2,device3,device4,device5])

print()
pprint(lab_devices)
print()

filename = "devices.yml"
with open(filename, "wt") as f:
    yaml.dump(lab_devices, f, default_flow_style=False)
