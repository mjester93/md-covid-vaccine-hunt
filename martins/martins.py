import requests

cookies = {
    'ASP.NET_SessionId': 'jyz3aut1rcmer3e440mtsruh',
    '.ASPXAUTH': '916045D57D04C7243D47DE96A6F9B7A6EE31E2658DFB4C51CE06FB65D8D3EA958C2D5F3A8BCA2E78D887E8DAD234AA3411F6CE411FDB638F13C9F1B7104180EA52EA59BAACFFA1E53BDE6B72D9C3C16DAFEFB46AFF685D9CE45B0E151DC232E1E9D021E233E5BDEE050B37C53B2A410C01F561B7C08E8C82581F12E48606AC94',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://martinssched.rxtouch.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://martinssched.rxtouch.com/rbssched/program/covid19/Patient/Schedule?zip=21740&appointmentType=5959',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
}

data = {
  'facilityId': '51117',
  'month': '3',
  'year': '2021',
  'snapCalendarToFirstAvailMonth': 'false'
}

response = requests.post(
    'https://martinssched.rxtouch.com/rbssched/program/covid19/Calendar/PatientCalendar',
    headers=headers, cookies=cookies, data=data)

json = response.json()
days = json.get("Data").get("Days")
goto_url = "https://martinssched.rxtouch.com/rbssched/program/covid19/Patient/Advisory"

for day in days:
    available = day.get('Available')

    if available:
        print(f"Martin's #6104 has available doses -- 1729 DUAL HIGHWAY HAGERSTOWN, MD 21740")
        print(f"{goto_url}")
        break
