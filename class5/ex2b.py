from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/')

my_devices = {
    "nxos1": {
        "intf_port": 1,
        "intf_addr": "10.1.100.1",
        "netmask": 24,
        "local_as": 22,
        "peer_ip": "10.1.100.2",
        },
    "nxos2": {
        "intf_port": 1,
        "intf_addr": "10.1.100.2",
        "netmask": 24,
        "local_as": 22,
        "peer_ip": "10.1.100.1",
        },
}

template_file = "nxos_intf_bgp.j2"
j2_template = env.get_template(template_file)
for device in my_devices:
    print("---- ",device," ----")
    output = j2_template.render(**my_devices[device])
    print(output)
