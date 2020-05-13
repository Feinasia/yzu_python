import json
import requests

news_title =[]
url = 'http://oldpaper.g0v.ronny.tw/index/json?fbclid=IwAR1zip-1_wLBrsZ2p9RfiAjm-WeFaxb8UyI4nA-uXOhK6Q3Wkgn7D_Zukow'
data = json.loads(requests.get(url).text)
#print(data)

for d in data.get('data'):
    dict={'title':d.get('title'), 'headlines':d.get('headlines')}
    news_title.append(dict)
#print(news_title)

file = open('news.txt', 'a', encoding='UTF-8')
for news in news_title:
    for head in news['headlines']:
        #print(head[1])
        if '譚德塞' in head[1]:
            print(head)
            file.writelines(head)
            file.write('\n')