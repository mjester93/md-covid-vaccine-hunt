import requests
import json
import os

locations_path = "\\".join([os.getcwd(), "locations.json"])

with open(locations_path) as f:
    locations = json.load(f)

base_url = "https://www.samsclub.com/api/node/vivaldi/v1/slots/club/"
goto_url = "https://www.samsclub.com/pharmacy/immunization?imzType=covid"

headers = {
    'authority': 'www.samsclub.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9,es;q=0.8',
}

params = (
    ('membershipType', 'BASE'),
    ('numOfDays', '6'),
    ('serviceType', 'IMMUNIZATION'),
)

for store in locations:
    store_num = store.get("store_id")
    address = store.get("address")

    response = requests.get(f"{base_url}{store_num}", headers=headers,
                            params=params)
    json = response.json()

    slots = json['payload']['slotDetails']

    for slot in slots:
        if slot['status'] != 'UNAVAILABLE':
            print(f"Sam's Club #{store_num} has available doses -- {address}")
            print(f"{goto_url}\n")
            break
