import pytest
import yaml
from testpage import OperationsHelper
import time

with open('config.yaml') as f:
    testdata = yaml.safe_load(f)

def test_cotact(browser):
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


if __name__ == '__main__':
    pytest.main(['-v'])


