from os import path
import yaml
from netmiko import ConnectHandler
from pprint import pprint
from ciscoconfparse import CiscoConfParse
import re

bgp_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

bgp_list = []

cisco_bgp = CiscoConfParse(bgp_config.splitlines(), ignore_blank_lines=False)
router_id = cisco_bgp.find_objects(r"^router")
router_id = router_id[0]
neighbor = router_id.re_search_children(r"neighbor")
remote = neighbor[0].children

for neig in neighbor:
    # print(neig.text)
    for remotes in neig.children:
        if re.match(r"^\s\s+remote-as", remotes.text):
            bgp_list.append((neig.text.split()[1],remotes.text.split()[1]))
            # print(remotes.text)

print(bgp_list)
