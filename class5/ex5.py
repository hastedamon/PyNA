from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/')

run_config = {
        "ntp_primary": "130.126.24.24",
        "ntp_secondary": "152.2.21.1",
        "timezone": "PST",
        "timezone_offset": "-8",
        "timezone_dst": "PDT",
        }

template_vars = { "run_config": run_config }
template_file = "cisco3_config.j2"
j2_template = env.get_template(template_file)
output = j2_template.render(**run_config)
print(output)
