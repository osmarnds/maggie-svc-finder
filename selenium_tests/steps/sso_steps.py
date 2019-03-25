from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium_tests.steps.utils import WaitForSSO

@given(u'An user is not authenticated')
def step_impl(context):
    pass

@when(u'he enters the web application')
def step_impl(context):
    context.driver.get(context.APPLICATION_URL)

@then(u'he gets authenticated')
def step_impl(context):
    WebDriverWait(context.driver, 60).until(WaitForSSO())
    assert context.driver.get_cookie('auth_token') is not None
