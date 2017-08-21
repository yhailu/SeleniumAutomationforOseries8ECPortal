"""
Created on Mar 11, 2017.

@author: Uma Pillai
"""
from . import selenium_driver


class BasePageTest(object):

    """Base class to initialize the base page that will be called from all pages."""

    def _setUp_Test(self, url, browser):
        """Set up - Initializing test."""
        self.verificationErrors = []

        self.driver = selenium_driver.connect(url, browser)
        self.base_url = selenium_driver.base_url

        print "base_url:", self.base_url

    def _tearDown_Test(self):
        """Tear down - Clean up test."""
        print "Close browser and quit"
        self.driver.close()
        self.driver.quit()


class KeywordNotDeclaredException(Exception):
    pass
