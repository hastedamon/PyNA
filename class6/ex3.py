import pyeapi
from pprint import pprint
from getpass import getpass
from my_funcs import read_yaml,show_arp

arista_passwd = getpass()

arista = read_yaml()
connection = pyeapi.client.connect(password=arista_passwd,**arista['arista4'])
device = pyeapi.client.Node(connection)

output = device.enable(["show ip route"])
routes = output[0]['result']['vrfs']['default']['routes']

for route,info in routes.items():
    print("-"*40)
    if info['routeType'] == 'static':
        nexthop = info['vias'][0]['nexthopAddr']
        pprint("Static route : "+route)
        pprint("Next Hop : "+nexthop)
        print("-"*40)
    elif info['routeType'] == 'connected':
        pprint("Connected route : "+route)
        print("-"*40)
