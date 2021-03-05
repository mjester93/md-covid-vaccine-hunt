import requests
import json
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

start_date = datetime.now().strftime("%Y-%m-%d")
end_date = (date.today() + relativedelta(months=+1)).strftime("%Y-%m-%d")

headers = {
    'authority': 'api-massvax.maryland.gov',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'x-correlation-id': 'c6d94702-9704-470b-9c70-ed3c0b4caad7',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://massvax.maryland.gov',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://massvax.maryland.gov/',
    'accept-language': 'en-US,en;q=0.9,es;q=0.8',
    'cookie': 'LPVID=IwNDM4NzA2ZjY5NmMzYWZi; LPSID-71510142=5PizcNRuR-W9PKW4bpBGHA',
}

data = '{"startDate":"' + start_date + '","endDate":"' + end_date + '","vaccineData":"WyJhMVYzZDAwMDAwMDAyMmdFQUEiXQ==","doseNumber":1,"url":"https://massvax.maryland.gov/appointment-select"} '

response = requests.post('https://api-massvax.maryland.gov/public/locations/a0Z3d000000HCTiEAO/availability',
                         headers=headers, data=data)

response_json = response.json()
availability = response_json['availability']

for x in availability:
    avail = x['available']

    if avail:
        print(f"Six Flags has available doses -- 13710 Central Ave, Bowie, MD 20721")
        print(f"https://massvax.maryland.gov/\n")
        break
