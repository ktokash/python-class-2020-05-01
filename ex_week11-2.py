"""import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    url = 'https://netbox.lasthop.io/api/'
    #http_headers = {'accept': "application/json; version=2.4"}
    http_headers = {'accept': "application/json"}
    response = requests.get(url, headers=http_headers, verify=False)
    # convert to a python data structure by just ... assigning it
    response2 = response.json()
    status = response.status_code
    text = response.text
    r_headers = response.headers
    
    
    print()
    print("response is:")
    pprint(response2)
    print("status is:")
    pprint(status)
    print("text is:")
    pprint(text)
    print("r_headers is:")
    pprint(r_headers)
    print()
"""


import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    url = "https://netbox.lasthop.io/api/"
    # http_headers = {'accept': "application/json; version=2.4"}
    # http_headers = {'accept': "application/json"}
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    response = requests.get(url, headers=http_headers, verify=False)
    # convert to a python data structure by just ... assigning it
    response2 = response.json()
    status = response.status_code
    text = response.text
    r_headers = response.headers

    print()
    print("response is:")
    pprint(response2)
    print("status is:")
    pprint(status)
    print("text is:")
    pprint(text)
    print("r_headers is:")
    pprint(r_headers)
    print()
