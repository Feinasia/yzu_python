import json
import requests

url ='https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json'
data = json.loads(requests.get(url).text)
#print(Ubike)
Ubike = data.get('result').get('records')

sbi = 30
bemp = 30
for yb in Ubike:
    if int(yb.get('sbi')) >= sbi and int(yb.get('bemp')) >= bemp:
        print(yb.get('sna'), yb.get('sbi'), yb.get('bemp'))

