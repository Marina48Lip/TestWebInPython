import pytest
import yaml
import time
from module import Site

with open('config.yaml') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])

selector_name = '//*[@id="login"]/div[1]/label/input'
input_name = site.find_element(mode='xpath', path=selector_name)
input_name.send_keys(testdata["username"])

selector_pass = '//*[@id="login"]/div[2]/label/input'
input_pass = site.find_element(mode='xpath', path=selector_pass)
input_pass.send_keys(testdata["password"])

selector_click = '#login > div.submit.svelte-uwkxn9 > button'
button = site.find_element(mode='css', path=selector_click)
button.click()
time.sleep(testdata['sleep_time'])

selector_create = '#create-btn'
button1 = site.find_element(mode='css', path=selector_create)
button1.click()
time.sleep(testdata['sleep_time'])

selector_title = '//*[@id="create-item"]/div/div/div[1]/div/label/input'
input_title = site.find_element(mode='xpath', path=selector_title)
input_title.send_keys(testdata["title"])
time.sleep(testdata['sleep_time'])

selector_description = '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'
input_description = site.find_element(mode='xpath', path=selector_description)
input_description.send_keys(testdata["description"])
time.sleep(testdata['sleep_time'])

selector_content = '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'
input_content = site.find_element(mode='xpath', path=selector_content)
input_content.send_keys(testdata["content"])
time.sleep(testdata['sleep_time'])

selector_click_save = '//*[@id="create-item"]/div/div/div[7]/div/button/span'
button_save = site.find_element(mode='xpath', path=selector_click_save)
button_save.click()
time.sleep(testdata['sleep_time'])

def test_find():
    findly_text = '//*[@id="app"]/main/div/div[1]/h1'
    findly = site.find_element(mode='xpath', path=findly_text)
    text = findly.text
    assert text == 'Test selenium'

if __name__ == '__main__':
    pytest.main(['-v'])


