from testpage_1 import OperationsHelper
import logging
import time


def test_step1(browser):
    logging.info('Test Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('niko2101')
    testpage.enter_pass('87c2463fae')
    testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(3)
    testpage.enter_name('Nikolay Eremeev')
    testpage.enter_email('test@mail.ru')
    testpage.enter_content('Test information')
    time.sleep(3)
    testpage.click_contact_us_button()
    time.sleep(3)
    assert testpage.alert() == 'Form successfully submitted'
