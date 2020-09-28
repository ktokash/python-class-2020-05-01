import os
import requests
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = 'https://netbox.lasthop.io/api/'
ADDRESS_ID = input("Enter address of object created in ex 4 (it was 205):")

if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    resp = requests.get(f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}", headers=http_headers, verify=False)
    # returns dict
    results = resp.json()
    pprint(results)

    # Reset headers to "Content-Type" for PUT
    http_headers = {
        'Content-Type': 'application/json; version=2.4;',
        'authorization': 'Token {}'.format(token),
    }


    data = {"address": "192.0.2.117/32", "description": "REST-API testing3"}
    response = requests.put(
        # Post to 'url', pass in headers, pass in data as json via json.dumps
        # using the post_data dictionary
        f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}/",
        headers=http_headers,
        data=json.dumps(data),
        verify=False
        )

    print()
    print(f"Response code: {resp.status_code}")
    print("Returned JSON:")
    resp = requests.get(f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}", headers=http_headers, verify=False)
    # returns dict
    results = resp.json()
    pprint(results)
    print()
