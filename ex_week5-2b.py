from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

nxos1_vars = {
    'name': 'nxos1',
    'interface': 'Ethernet1/1',
    'ip_address': '10.1.100.1',
    'netmask': '24',
    'local_as': '22',
    'peer_ip': '10.1.100.2',
}

nxos2_vars = {
    'name': 'nxos2',
    'interface': 'Ethernet1/1',
    'ip_address': '10.1.100.2',
    'netmask': '24',
    'local_as': '22',
    'peer_ip': '10.1.100.1',
}

devices = [nxos1_vars, nxos2_vars]

for device in devices:
    my_template = 'j2_template_ex5-2b.j2'
    j2_template = env.get_template(my_template)
    output = j2_template.render(**device)
    print(output)

