import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}
cookies = {
    "CRID": "dNcXa4ibYBW28sMU",
    "C_GAMEID": "456",
    "C_S_GAMEID": "10",
    "__root_domain_v": ".bijiaqi.com",
    "_qddaz": "QD.194150210410802",
    "_qdda": "3-1.1",
    "_qddab": "3-kp21yg.l23go681",
    "_qddac": "3-1.1.kp21yg.l23go681",
    "unv": "17"
}
url = "http://www.bijiaqi.com/"
response = requests.get(url, headers=headers, cookies=cookies, verify=False)

print(response.text)
print(response)