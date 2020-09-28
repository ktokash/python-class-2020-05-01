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

    # Change .get method to .delete
    response = requests.delete(f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}", headers=http_headers, verify=False)
    
    if response.ok:
        print("device deleted successfully")
    
    resp = requests.get(f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}", headers=http_headers, verify=False)
    # returns dict
    results = resp.json()
    pprint(results)

