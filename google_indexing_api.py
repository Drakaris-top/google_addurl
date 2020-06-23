"""
1) В папку со скриптом поместить ключ и назвать его addurl.json
2) В папке со скриптом создать файл 'urls.txt' в него поместить урлы
"""

from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json

def googlebot_idi_syuda(url):
    JSON_KEY_FILE = "addurl.json"
    SCOPES = ["https://www.googleapis.com/auth/indexing"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
    http = credentials.authorize(httplib2.Http())


    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


    content = {}
    content['url'] = url
    content['type'] = "URL_UPDATED"
    json_ctn = json.dumps(content)

    response, content = http.request(ENDPOINT, method="POST", body=json_ctn)

    result = json.loads(content.decode())
    return result

urls = []
with open('urls.txt') as f:
    for line in f:
        url.append(line.strip())

for url in urls:
    add_url = googlebot_idi_syuda(url)
    print(add_url)

input('Все урлы отправлены, свечка в церкви поставлена, жди')
