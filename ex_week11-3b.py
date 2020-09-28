import os
import requests
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = 'https://netbox.lasthop.io/api/'

if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    resp = requests.get(f"{BASE_URL}dcim/devices/", headers=http_headers, verify=False)
    # returns a list of dictionaries
    results = resp.json()["results"]
    
    # See what comes back, which is a list of dicts
    '''for dev in results:
        print()
        pprint(results)'''


    devices = []
    for dev in results:
    #    devices.append(dev["display_name"])
        print()
        print("-" * 60)
        print(dev["display_name"])
        print("-" * 10)
        print("Location:", dev["site"]["name"])
        print("Vendor:", dev['device_type']['manufacturer']['name'])
        print("Status:", dev['status']['label'])
        print("-" * 60)
        print()

