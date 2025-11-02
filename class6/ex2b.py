import pyeapi
from getpass import getpass
from my_funcs import read_yaml,show_arp

arista_passwd = getpass()

arista = read_yaml()
connection = pyeapi.client.connect(password=arista_passwd,**arista['arista4'])

device = pyeapi.client.Node(connection)
show_arp(device)
