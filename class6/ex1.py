import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable(["show ip arp"])
arp_list = output[0]['result']['ipV4Neighbors']

for arp in arp_list:
    print(arp['address']," ---> ",arp['hwAddress'])

