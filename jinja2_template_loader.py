from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

template_vars = {}

template_file = 'j2_vars.j2'
template = env.get_template(template_file)
output = template.render(**template_vars)
print(output)
