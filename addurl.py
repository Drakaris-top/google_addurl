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
    content['url'] = f'http://0core.ru/?r={url}'
    content['type'] = "URL_UPDATED"
    json_ctn = json.dumps(content)
    # print(json_ctn);return

    response, content = http.request(ENDPOINT, method="POST", body=json_ctn)

    result = json.loads(content.decode())
    return result

domains = []
with open('domains.txt') as f:
    for line in f:
        domains.append(line.strip())

for domain in domains:
    add_url = googlebot_idi_syuda(domain)
    print(add_url)

input('Все урлы отправлены, свечка в церкви поставлена, жди')