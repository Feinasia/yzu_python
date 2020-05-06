import json
import requests

url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'  # Bad rices
url2 = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceQualified.aspx'  # Good rices
r = requests.get(url)
r2 = requests.get(url2)
#print(r.status_code)  #200 為有網頁的  code
#print(r.text)

bad_rices = json.loads(r.text)
for br in bad_rices:
    if "壽司" in br.get('品名'):
        print(br.get('品名'), br.get('廠商名稱'), br.get('不合格原因'))

good_rices = json.loads(r2.text)
for gr in good_rices:
    if "糙米" in gr.get('品名'):
        print(gr.get('品名'), gr.get('廠商名稱'))