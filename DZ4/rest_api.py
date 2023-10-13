
import requests as requests
import yaml

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)

def get_token():
    response = requests.post(url=conf['url_login'],
                              data={'username': conf['username'],
                                     'password': conf['password']})
    return response.json()['token']
def get(token):
    response = requests.get(conf["url_posts"],
                        headers={"X-Auth-Token": token},
                        params={"owner": "notMe"})
    return response.json()

if __name__ == '__main__':
    temp = get_token()
    print(get(temp))

