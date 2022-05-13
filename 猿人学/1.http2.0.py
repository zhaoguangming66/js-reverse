import json
import requests
import httpx

header = {
    "cookie": 'qpfccr=true; no-alert3=true; tk=-3538640823032487587; sessionid=akkp0426hfqtca4o8ff3juqh7144v2xy',
    'user-agent': 'yuanrenxue.project'
}
# c = httpx.Client(http2=True)
n = 0
c= requests.Session()
for page in range(1, 6):
    url = f'https://match.yuanrenxue.com/api/match/17?page={page}'
    res = c.get(url, headers=header)
    data = res.content.decode()
    print(data)
    data=json.loads(data)
    for item in data["data"]:
        n+=item["value"]
print(n)