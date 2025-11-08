import yaml
import os
import pyeapi

def read_yaml(filename):
    with open(filename, "r") as f:
        return yaml.safe_load(f)

def show_arp(device):
    output = device.enable(["show ip arp"])
    arp_list = output[0]['result']['ipV4Neighbors']
    for arp in arp_list:
        print(arp['address']," ---> ",arp['hwAddress'])

