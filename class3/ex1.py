import re
from pprint import pprint

# arp = '''
# Protocol Address Age Hardware Addr Type Interface Internet 10.220.88.1 67 0062.ec29.70fe ARPA Gi0/0/0 Internet 10.220.88.20 29 c89c.1dea.0eb6 ARPA Gi0/0/0 Internet 10.220.88.22 - a093.5141.b780 ARPA Gi0/0/0 Internet 10.220.88.37 104 0001.00ff.0001 ARPA Gi0/0/0 Internet 10.220.88.38 161 0002.00ff.0001 ARPA Gi0/0/0'''

arp_data = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.220.88.1            67   0062.ec29.70fe  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.20           29   c89c.1dea.0eb6  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.22            -   a093.5141.b780  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.37          104   0001.00ff.0001  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.38          161   0002.00ff.0001  ARPA   GigabitEthernet0/0/0
"""

arp_words = arp_data.split()


the_list = []

for word in arp_words:
    if re.search(r'^10\.220\.88\.\d{1,3}$', word):
        device = {}
        ip_addr = word
    if re.search(r'\b([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}\b', word):
        mac_addr = word
    if re.search(r'Ethernet', word):
        intf_name = word
        device = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": intf_name}
        the_list.append(device)

print()
pprint(the_list)
print()

