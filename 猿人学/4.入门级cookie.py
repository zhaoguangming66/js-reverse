import requests

headers = {
    'user-agent': 'yuanrenxue.project',

    "tk": "-5707074668778874727",
    "sessionid": "9d2y9hbuzo1ox4o6x3zly18d70d8n7te",
}

session = requests.session()
data = session.get(url='https://match.yuanrenxue.com/match/13')
print(data.text)
data = (data.text.replace("<script>document.cookie=('", '').replace("')+('", '').replace(
    "')+';path=/';location.href=location.pathname+location.search</script>", '')).split('=')
cookie = {
    data[0]: data[1]
}
session.cookies.update(cookie)

url = 'https://match.yuanrenxue.com/api/match/13?page=4'

data = session.get(url)

print(session.cookies["yuanrenxue_cookie"], session.cookies['sessionid'], session.cookies)
print(data.text)
