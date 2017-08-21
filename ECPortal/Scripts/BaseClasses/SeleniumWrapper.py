"""
Created on Mar 10, 2017.

@author: Uma Pillai
"""

from selenium import webdriver


class SeleniumWrapper:

    """Selenium wrapper class."""

    def connect(self, url, browser):
        """Connect browser through selenium."""

        print "connecting", url, browser
        self.driver = None
        if browser == "InternetExplorer":
            self.driver = webdriver.Ie()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif browser == "Chrome":
            self.driver = webdriver.Chrome()
        if not self.driver:
            print "Webdriver for", browser, "needs to be added"
            assert False

        self.base_url = url

        return self.driver
