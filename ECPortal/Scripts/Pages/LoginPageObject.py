'''
Created on Mar 10, 2017

@author: Uma Pillai
'''
from BaseClasses.BasePageObject import BasePageObject
from Locators import locators
from UIClasses.UIElements import TextBoxElement, ButtonElement, LinkElement
import time


class LoginPageObject(BasePageObject):

    username = TextBoxElement("login.username")
    password = TextBoxElement("login.password")
    loginButton = ButtonElement('login.login.button')

    def __init__(self, driver):
        super(LoginPageObject, self).__init__(driver)

        loginLink = LinkElement("login.login.link")

        loginLink.click()

        # assert (locators["ECPLaunchPageTitle"] == self.driver.title), (
        #   "Title Mismatch: " + locators["ECPLaunchPageTitle"] + " != " + self.driver.title)

    def login(self, username, password):
        time.sleep(2)
        self.username = username
        self.password = password
        self.loginButton.click()
        time.sleep(2)

    def submit(self):
        submitButton = ButtonElement("login.submit.button")
        submitButton.click()
        time.sleep(5)
        assert (locators["ECPLoginPageTitle"] == self.driver.title), (
            "Title Mismatch: " + locators["ECPLoginPageTitle"] + " != " + self.driver.title)

    def logout(self):
        logoutLink = LinkElement("login.logout.link")
        logoutLink.click()
        time.sleep(5)

        assert (locators["ECPLogoutPageTitle"] == self.driver.title), (
            "Title Mismatch: " + locators["ECPLogoutPageTitle"] + " != " + self.driver.title)
