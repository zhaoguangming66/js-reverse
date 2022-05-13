import requests
import execjs


def js_from_file():
    """
    读取js文件
    :return:
    """
    with open('jsfock.js', 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def get_signature():
    data = js_from_file()
    ctx = execjs.compile(data)
    return ctx.call('get')


def get_page(num):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://spider.wangluozhe.com",
        "Pragma": "no-cache",
        "Referer": "http://spider.wangluozhe.com/challenge/4",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    cookies = {
        "session": "fa60fe13-1209-4592-8255-0faca8f29e32.nSUuFr03-MfaY5HxSbR7my-i1BU"
    }
    url = "http://spider.wangluozhe.com/challenge/api/4"
    data = {
        "page": num,
        "count": "10",
        "_signature": get_signature()
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)

    return response.content.decode()


if __name__ == '__main__':
    print(get_page(1))
