from jinja2 import Template

bgp_config = """
router bgp {{ bgp_as }}
 bgp router-id {{ router_id }}
 bgp log-neighbor-changes
 neighbor {{ peer1 }} remote-as 44
"""

example_expr = """
some text with expressions {{ 13 + 3 }}
other expressions {{ 13 * 7 }}
hello
"""

my_template = bgp_config
#my_template = example_expr
# Call the Template class, pass in bgp_config string
j2_template = Template(my_template)
# Results in object called j2_template, we call the render function on it
output = j2_template.render()
output = j2_template.render(bgp_as=22, router_id="1.1.1.1", peer1="2.2.2.2")
print()
print(output)
