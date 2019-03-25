from jwt import encode
from app.config import config
from selenium.common.exceptions import JavascriptException

class WaitForSSO():
    ''' Selenium class that blocks SSO is done '''

    def __call__(self, driver):
        if driver.get_cookie('auth_token') is not None:
            return True
        return False

class WaitForAngularInit():
    ''' Selenium class that blocks until Angular is loaded '''

    def __call__(self, driver):
        try:
            if driver.execute_script('return typeof angular') == 'undefined':
                return False
            if driver.execute_script('return typeof angular.element(document).injector') == 'undefined':
                return False
        except JavascriptException:
            return False
        return True

class WaitForAngularHttp():
    ''' Blocks until all Angular $http calls are finished '''

    SCRIPT = '''
        var callback = arguments[arguments.length - 1];
        var el = document.querySelector('html');
        if (!window.angular) {
            callback('false')
        }
        if (angular.getTestability) {
            angular.getTestability(el).whenStable(function(){callback('true')});
        } else {
            if (!angular.element(el).injector()) {
                callback('false')
            }
            var browser = angular.element(el).injector().get('$browser');
            browser.notifyWhenNoOutstandingRequests(function(){callback('true')});
        };
    '''
    def __call__(self, driver):
        try:
            return driver.execute_async_script(self.SCRIPT)
        except JavascriptException:
            return False

def impersonate(driver, username):
    ''' Sets cookie to impersonate another user '''
    driver.delete_all_cookies()
    driver.add_cookie({
        'name': 'auth_token',
        'value': encode({'sub': username}, config.JWT_KEY).decode('UTF-8'),
        'path': '/'
        }
    )
