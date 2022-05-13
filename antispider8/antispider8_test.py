import json
import requests
import execjs


def js_from_file():
    """
    读取js文件
    :return:
    """
    with open('antitest.js', 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def get_data():
    ctx = execjs.compile(js_from_file())
    data = ctx.call('getpass')
    return data


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://antispider8.scrape.center/page/6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
}


def get_detil(page):
    url = "https://antispider8.scrape.center/api/movie/"
    params = {
        "limit": "10",
        "offset": page,
        "token": get_data()
    }
    response = requests.get(url, headers=headers, params=params)
    return response.content.decode()


def detil_json(data):
    data1=json.loads(data)
    for item in data1["results"]:
        print("id",item["id"])
        print("name",item["name"])
        print("alias",item["alias"])
        print("cover",item["cover"])
        print("categories",item["categories"])
        print("published_at",item["published_at"])
        print("minute",item["minute"])
        print("regions", item["regions"])




if __name__ == '__main__':
    data = (page for page in range(0, 100, 10))
    for page in data:
        json_data = get_detil(page)
        detil_json(json_data)
