import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_report import sendemail

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


# фикстура действует всю сессию
@pytest.fixture(scope='session')
def browser():
    # инициаоизация firefox
    if testdata['browser'] == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    # инициализация chrome
    elif testdata['browser'] == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
    sendemail()




@pytest.fixture()
def token():
    result = requests.post(url=testdata["url"], data={"username": testdata["login"],
                                                      "password": testdata["password"]})
    return result.json()["token"]