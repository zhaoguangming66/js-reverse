import json
import requests
import httpx

header = {
    "cookie": 'qpfccr=true; no-alert3=true; tk=-241171568113441120; sessionid=eni4i97xy1fu580eitniz64jfnhmx13z',
    'user-agent': 'yuanrenxue.project'
}
# c = httpx.Client(http2=True)
key_dict={
    '1':"E",
'2':"I",
'3':"M",
'4':"Q",
'5':"V",
}
n = 0
c= requests.Session()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for num,page in key_dict.items():
    url = f'https://match.yuanrenxue.com/api/match/12?page={num}&m=eXVhbnJlbnh1ZT{page}%3D'
    print(url)
    try:

        res = c.get(url, headers=header)
        data = res.content.decode()
        data = json.loads(data)
        for item in data["data"]:
            n += item["value"]
    except:
        print('成功',page)
print(n)