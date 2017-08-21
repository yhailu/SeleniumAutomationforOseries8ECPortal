"""
Created on Mar 10, 2017.

@author: Uma Pillai
"""
from Locators import locators
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import selenium_driver


class BasePageElement(object):

    """Base class for UI elements."""

    def __init__(self, locator):
        """Initialise element."""
        self.findBy = locators[locator][0]
        self.locator = locators[locator][1]

    def __set__(self, obj, value):
        """Set the text to the value supplied."""
        driver = selenium_driver.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, value):
        """Get the text of the specified object."""
        driver = selenium_driver.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        value = element.get_attribute("value")
        return value

    def is_visible(self):
        """ return True if element is visible within 5 seconds, otherwise False """
        driver = selenium_driver.driver
        try:
            WebDriverWait(
                driver, 5).until(
                EC.presence_of_element_located(
                    (self.findBy, self.locator)))
            return True
        except:
            return False

    def wait(self):
        driver = selenium_driver.driver
        try:
            WebDriverWait(
                driver, 10).until(
                EC.presence_of_element_located(
                    (self.findBy, self.locator)))
            return True
        except:
            return False
        pass


class NoSuchElementException(Exception):
    pass


def highlight(element):
    """Highlight a UI element."""
    driver = element._parent

    def apply_style(s):
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1])",
            element,
            s)
    original_style = element.get_attribute('style')
    apply_style("border: 4px solid red")
    if (element.get_attribute("style") is not None):
        time.sleep(2)
    apply_style(original_style)
