import requests
import json
import os

locations_path = "\\".join([os.getcwd(), "locations.json"])

with open(locations_path) as f:
    locations = json.load(f)

base_url = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber="
goto_url = "https://www.riteaid.com/pharmacy/apt-scheduler"

for store in locations:
    store_num = store.get("store_number")
    address = store.get("address")

    url = f"{base_url}{store_num}"
    r = requests.get(url)
    json = r.json()

    slots = json['Data']['slots']
    first_dose = slots['1']
    second_dose = slots['2']

    if first_dose:
        print(f"Rite Aid #{store_num} has available doses -- {address}")
        print(f"{goto_url}")

