"""
Created on Mar 10, 2017.

@author: Uma Pillai
"""


class BasePageObject(object):

    """Base class for Page Objects."""

    def __init__(self, selenium_driver):
        """Initialise page."""
        self.driver = selenium_driver
        self.timeout = 30
#         self.driver.get(base_url)
#         self.driver.maximize_window()

    def launchURL(self, url):
        self.driver.get(url)
#         self.saveCookies()
        self.driver.maximize_window()

    def saveCookies(self):
        self.cookies = self.driver.get_cookies()
        print self.cookies
        import pickle
        pickle.dump(
            self.driver.get_cookies(),
            open(
                "ECPortalCookies.pkl",
                "wb"))

    def loadCookies(self, url):
        import pickle
        self.driver.get(url)
        for cookie in pickle.load(open("ECPortalCookies.pkl", "rb")):
            self.driver.add_cookie(cookie)
