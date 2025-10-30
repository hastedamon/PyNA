from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/')

vrf_vars = [ 
    {
        "vrf_name": "blue",
        "rd_number": "100:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
        },
    {
        "vrf_name": "red",
        "rd_number": "100:2",
        "ipv4_enabled": True,
        "ipv6_enabled": False,
        },
    {
        "vrf_name": "yellow",
        "rd_number": "100:3",
        "ipv4_enabled": False,
        "ipv6_enabled": True,
        },
    {
        "vrf_name": "green",
        "rd_number": "100:4",
        "ipv4_enabled": True,
        "ipv6_enabled": False,
        },
    {
        "vrf_name": "black",
        "rd_number": "100:5",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
        },
    ]

template_vars = { "vrf_config": vrf_vars }
template_file = "ex4_vrf.j2"
j2_template = env.get_template(template_file)
output = j2_template.render(**template_vars)
print(output)
