from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/')

vrf_config = {
    "vrf_name": "blue",
    "rd_number": "100:1",
    "ipv4_enabled": True,
    "ipv6_enabled": True,
    }


template_file = "ex3_vrf.j2"
j2_template = env.get_template(template_file)
output = j2_template.render(**vrf_config)
print(output)
