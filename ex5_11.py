from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

# Create dict instead of normal variable
arp_entry = {
    "interface": "mgmt0",
    "ip": "10.0.0.72",
    "mac": "1c:2c:3c:4c:5c:6c",
    "age": 140.0
}

template_vars = {
    "arp_entry": arp_entry,
}

template_file = 'j2template2.j2'
template = env.get_template(template_file)
output = template.render(**template_vars)
print(output)
