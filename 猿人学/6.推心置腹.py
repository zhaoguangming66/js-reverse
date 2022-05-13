import requests
s=requests.session()
headers = {
    "authority": "match.yuanrenxue.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.com/match/3",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "qpfccr": "true",
    "no-alert3": "true",
    "tk": "-484719995528746790",
    "sessionid": "zys7um2dewk5h6f47ijh15fb5rhg0xu5",
    "m": "pua"
}
url = "https://match.yuanrenxue.com/api/answer"


def get_data(num):
    params = {
        "answer": num,
        "id": "3"
    }
    response = s.get(url, headers=headers, cookies=cookies, params=params)

    date = response.json()
    if date['info'] != 'failed':
        print(num,'成功成功')
    else:
        print(f'{num}错误')


if __name__ == '__main__':
    for num in range(1000, 9999):
        get_data(num)
