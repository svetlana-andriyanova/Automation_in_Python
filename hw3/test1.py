import yaml
from testPage import OperationsHelper
import logging

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test 1')
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pswd('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step2(browser):
    logging.info('Test 2')
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pswd(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_login_text() == 'Blog'


def test_step3(browser):
    logging.info('Test 3')
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.click_new_post_button()
    testpage.enter_title_post(testdata["title"])
    testpage.enter_description_post(testdata["discription"])
    testpage.enter_content_post(testdata["content"])
    testpage.click_save_new_post_button()
    assert testpage.check_exist_post() == 'Yo ho ho'


# ДЗ№3 Форма CONTACT US
def test_step4(browser):
    logging.info('Test 4')
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.click_contactus_button()
    testpage.enter_name_field('test_name')
    testpage.enter_email_field(testdata['test_email'])
    testpage.enter_content_field('any content')
    testpage.click_contactus_send_button()
    assert testpage.text_alert() == 'Form successfully submitted'