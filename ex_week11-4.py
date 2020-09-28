import os
import requests
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = 'https://netbox.lasthop.io/api/ipam/ip-addresses/'

if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    
    # define the object we're creating
    post_data = {
        "address": "192.0.2.117/32"
        }
    
    response = requests.post(
        # Post to 'url', pass in headers, pass in data as json via json.dumps
        # using the post_data dictionary
        f"{BASE_URL}", headers=http_headers, data=json.dumps(post_data), verify=False
        )
    
    response = response.json()
    print()
    pprint(response)
    # print(response._content.decode())
    print()

