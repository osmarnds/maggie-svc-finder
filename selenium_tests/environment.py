from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium_tests.steps.utils import WaitForSSO, WaitForAngularInit, WaitForAngularHttp

APPLICATION_URL = r'https://corphr-flask-architecture-dev.ausvdc02.pcf.dell.com'

def before_all(context):
    context.APPLICATION_URL = APPLICATION_URL
    browser = context.config.userdata.get('browser')
    if browser is None or browser == 'ie':
        print('\n  RUNNING SELENIUM TESTS ON IE  \n')
        ie_options = webdriver.IeOptions()
        ie_options.require_window_focus = True
        ie_options.element_scroll_behavior = 1
        ie_options.native_events = False
        ie_options.ignore_protected_mode_settings = True
        ie_options.ignore_zoom_level = True
        ie_options.persistent_hover = True
        context.driver = webdriver.Ie(capabilities={'ie.ensureCleanSession': True}, options=ie_options)
    elif browser == 'edge':
        print('\n  RUNNING SELENIUM TESTS ON EDGE  \n')
        context.driver = webdriver.Edge(capabilities={'InPrivate': True})
    elif browser == 'chrome':
        print('\n  RUNNING SELENIUM TESTS ON CHROME  \n')
        context.driver = webdriver.Chrome()
    elif browser == 'firefox':
        # Firefox Profile that enables SSO
        print('\n  RUNNING SELENIUM TESTS ON FIREFOX  \n')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.tabs.remote.force-enable", True)
        fp.set_preference("network.negotiate-auth.trusted-uris", 'dell.com')
        fp.set_preference("network.negotiate-auth.delegation-uris", 'dell.com')
        fp.set_preference("network.automatic-ntlm-auth.trusted-uris", 'dell.com')
        context.driver = webdriver.Firefox(firefox_profile=fp)
    context.driver.get(APPLICATION_URL)

def before_step(context, step):
    WebDriverWait(context.driver, 60).until(WaitForSSO())
    WebDriverWait(context.driver, 30).until(WaitForAngularInit())
    WebDriverWait(context.driver, 60).until(WaitForAngularHttp())
