import pytest
import yaml
from testpage import OperationsHelper
import time
import logging
import requests
from rest_api import get

S = requests.Session()

with open('config.yaml') as f:
    testdata = yaml.safe_load(f)

def test_contact_us(browser):
    logging.info('Test contact us - started')
    value = OperationsHelper(browser)
    value.go_to_site()
    value.enter_login(testdata["username"])
    value.enter_password(testdata["password"])
    value.enter_button()
    value.enter_contact()
    time.sleep(2)
    value.enter_contact_us()
    time.sleep(2)
    value.alert()
    assert value.alert() == 'Form successfully submitted'

def test_step1(get_token):
    logging.info('Test ID - started')
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert 82485 in lst_id

def test_step2(get_token):
    logging.info('Test New post - started')
    assert (S.post(url=testdata['url_posts'], headers={'X-Auth-Token': get_token},
                 data={'title' : testdata['title'],
                         'description': testdata['description'],
                         'content': testdata['content']}).json())

if __name__ == '__main__':
    pytest.main(['-v'])


