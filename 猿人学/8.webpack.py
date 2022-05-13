import json

import requests
import execjs


def js_from_file():
    """
    读取js文件
    :return:
    """
    with open('sd.js', 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def get_data():
    ctx = execjs.compile(js_from_file())
    data = ctx.call('get_m')
    return data


def get_page(num):
    headers = {
        'user-agent': 'yuanrenxue.project',

    }
    cookies = {
        "tk": "5909947313675555232",
        "sessionid": "ip4urejudvy1vk30sbfnm8htm4i8lafd"
    }
    url = "https://match.yuanrenxue.com/api/match/16"
    data_lst = get_data()
    params = {
        "page": num,
        "m": data_lst[0],
        "t": data_lst[1]
    }
    print(params)
    jishi = 0
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    data = response.content.decode()
    data_json = json.loads(data)
    for ite in data_json['data']:
        jishi += ite['value']
    return jishi


if __name__ == '__main__':
    nums = 0
    for page in range(1,6):
        nums+=get_page(page)
    print(nums)
