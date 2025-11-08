import pyeapi
from pprint import pprint
from getpass import getpass
from my_funcs import read_yaml
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Load Arista devices dictionary from YAML file
def load_yaml(yaml_file="arista_devices_full.yml"):
  return read_yaml(yaml_file)

# Get interface configuration from Jinja2 template
def get_template(template_file="intf_config.j2"):
  env = Environment(undefined=StrictUndefined)
  env.loader = FileSystemLoader('./')
  return env.get_template(template_file)
  

def main():
  arista = load_yaml()
  output = {}
  aristas = ['arista1','arista2','arista3','arista4']
  arista_passwd = getpass()
  j2_template = get_template()

  for arista_n in aristas:
    # Establish connection to device arista_n
    connection = pyeapi.client.connect(password=arista_passwd,**arista[arista_n])
    device = pyeapi.client.Node(connection)
    # Prepare Interface commands from Jinja template
    cfg = j2_template.render(**arista[arista_n]['data'])
    cfg_lines = cfg.splitlines()
    # Configure interfaces
    cfg_interface = device.config(cfg_lines)
    # Run show command to check interfaces and append it to output
    output[arista_n] = device.enable(["show ip interface brief"])
    output_intf = output[arista_n][0]['result']['interfaces']
    for intf,intf_info in output_intf.items():
      if "Loopback" in intf:
        ip_address = intf_info['interfaceAddress']['ipAddr']['address']
        ip_mask = intf_info['interfaceAddress']['ipAddr']['maskLen']
        print(intf,": ",ip_address,"/",ip_mask)

if __name__ == "__main__":
  main()
