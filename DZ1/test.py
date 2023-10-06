from rest_api import get
import pytest
import yaml
import requests

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)

S = requests.Session()

def test_step1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert 81988 in lst_id

def test_step2(get_token):
    assert (S.post(url=conf['url_posts'], headers={'X-Auth-Token': get_token},
                 data={'title' : conf['title'],
                         'description': conf['description'],
                         'content': conf['content']}).json())

def test_step3(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["description"] for el in lst]
    assert 'New description' in lst_id


if __name__ == '__main__':
    pytest.main(['-v'])
