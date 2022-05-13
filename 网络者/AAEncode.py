import execjs
import requests
ssss=requests.session()


def js_from_file():
    """
    读取js文件
    :return:
    """
    with open('AAEncode.js', 'r', encoding='UTF-8') as file:
        result = file.read()
    ctx = execjs.compile(result)

    return ctx.call('getSign')


def get_date(num):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://spider.wangluozhe.com",
        "Pragma": "no-cache",
        "Referer": "http://spider.wangluozhe.com/challenge/3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    cookies = {
        "session": "fa60fe13-1209-4592-8255-0faca8f29e32.nSUuFr03-MfaY5HxSbR7my-i1BU"
    }
    url = "http://spider.wangluozhe.com/challenge/api/3"
    data = {
        "page": num,
        "count": "10",
        "_signature": js_from_file()
    }
    response = ssss.post(url, headers=headers, cookies=cookies, data=data, verify=False)

    return response.json()


def get_json(jso):
    js = 0
    for jd in jso['data']:
        js += jd['value']
    return js


def all_data():
    all_ = 0
    for page in range(1, 101):
        lit_dat = get_date(page)
        print(lit_dat)
        print(get_json(lit_dat))
        all_ += get_json(lit_dat)
    return all_

if __name__ == '__main__':
    print(all_data())
