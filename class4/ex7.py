import textfsm
from pprint import pprint

template_file = "ex2.template"
template = open(template_file)

with open("show_interface_status_ex1.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

interfaces = []

for interface in data:
    interfaces.append({'PORT_NAME':interface[0],'STATUS':interface[1],'VLAN':interface[2],'DUPLEX':interface[3],'SPEED':interface[4], 'PORT_TYPE':interface[5]})

pprint(interfaces)
