import yaml
import os
import pyeapi
from getpass import getpass

arista_yaml = "/home/david/PyNA/class6/arista_devices.yml"
arista_passwd = getpass()

with open(arista_yaml) as f:
    aristas = yaml.safe_load(f)

connection = pyeapi.client.connect(password=arista_passwd,**aristas['arista4'])

device = pyeapi.client.Node(connection)

output = device.enable(["show ip arp"])
arp_list = output[0]['result']['ipV4Neighbors']

for arp in arp_list:
    print(arp['address']," ---> ",arp['hwAddress'])

