from jinja2 import Template
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Create an jinja2 environment
#env = Environment(undefined=StrictUndefined)
# Load the j2 templates with FileSystemLoader class to find the templates
#env.loader = FileSystemLoader('.')

env = Environment(undefined=StrictUndefined)
# Call the loader function on the env object we just created with the Environment class
# Can list places to search
env.loader = FileSystemLoader([".", './templates/'])

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "3.2.2.2",
}

template_file = "bgp_config.j2"
# Instead of reading template in via python file handlers, use get_template
# and pass in the template file
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)
