'''
Created on Jul 3, 2017

@author: stetester
'''
from BaseClasses import selenium_driver
from BaseClasses.BasePageObject import BasePageObject
from UIClasses.UIElements import TextBoxElement, ButtonElement, LinkElement, CheckBoxElement,\
    DropDownListElement, DateElement, DatePickerElement, CanvasElement, LabelElement
from Utilities.ECP_PDFHandler import PDFHandler
import time

import pyautogui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# from Locators import locators
class CertificatePageObject(BasePageObject):

    createButton = ButtonElement('create.certificate')
    jurisdictionSelector = CheckBoxElement('select.jurisdiction')
    jurisdictionSelector2 = CheckBoxElement('select.jurisdiction.3')
    continueButton = ButtonElement('continue')
    saveButton = ButtonElement('save')
    formDropDown = DropDownListElement('certificate.form.dropdownlist')
    jurisdictionIssueDate = DateElement(
        'new.certificate.issue.date')
    jurisdictionIssueDatePicker = DatePickerElement(
        'new.certificate.issue.datepicker')
    signaturePad = CanvasElement('certificate.signature')
    renewButton = ButtonElement('renew.button')

    searchBox = TextBoxElement('search.box')
    stringFound = ButtonElement('first.row.from.search')
    completeButton = ButtonElement('complete.button')
    expirationDate = DateElement('renew.certificate.expiration.date')
    expirationDatePicker = DatePickerElement(
        'renew.certificate.expiration.datepicker')
    # initial pass does not implement expiration date
    #jurisdictionExpirationDate = DateElement('new.certificate.expiration.date')
    # jurisdictionExpirationDatePicker = DatePickerElement(
    #    'new.certificate.expiration.datepicker')

    def __init__(self, driver):
        super(CertificatePageObject, self).__init__(driver)
        self.cookies = self.driver.get_cookies()
        self.cookies_dict = {}
        for cookie in self.cookies:
            self.cookies_dict[cookie['name']] = cookie['value']
        print self.cookies_dict

    def create_newCertificate(
            self, jurisdiction, form, issueDate, expirationDate):
        """using time.sleep  a lot because if we don't wait in some cases the automation
        will fail because it does not identify the elements on the page quick enough"""
        print jurisdiction, form, issueDate
        self.createButton.click()
        time.sleep(4)

        self.jurisdictionSelector = jurisdiction
        self.jurisdictionSelector2 = jurisdiction

        self.continueButton.click()
        time.sleep(2)

        self.formDropDown = form
        self.continueButton.click()
        time.sleep(2)
        self.jurisdictionIssueDate = issueDate
        self.jurisdictionIssueDatePicker = issueDate
        self.continueButton.click()
        # initial pass does not implement expiration date
        #self.jurisdictionExpirationDate = expirationDate
        #self.jurisdictionExpirationDatePicker = expirationDate

    def renew_certificate(self, certNumber=None,
                          expirationDate=None):
        searchString = certNumber
        self.searchBox = searchString
        self.stringFound.click()
        self.stringFound.click()
        self.renewButton.click()
        time.sleep(2)
        self.expirationDate = expirationDate
        self.expirationDatePicker = expirationDate
        self.continueButton.click()
        print searchString
        # pick last day of the month

        pass

    def complete_certificate(self, certNumber=None):

        searchString = certNumber
        self.searchBox = searchString
        self.stringFound.click()
        self.stringFound.click()
        self.completeButton.click()

        pass

    def fill_pdf_form(self, csvFilePath):

        print "Cookies in fill_pdf_form", self.cookies_dict

        url = self.driver.current_url
        print url

        # Using PDF miner
        pdfObj = PDFHandler(url, cookies=self.cookies_dict)

        # Get all pdf fields. Returns name/value/bbox coords.
        # Use the names to create test data header
        pdfFields = pdfObj.resolve_pdf()

        from Utilities.csvLibrary import csvLibrary
        csvData = csvLibrary().read_csv_file(csvFilePath)
#         header = csvData[0]

        testData = csvData[0]

        pyautogui.PAUSE = 1

        # TODO: Need to find better way to click on the pdf.
        # something to set focus on the pdf
        x, y = 100, 100
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)

        pyautogui.press('tab')  # Focus on Clear Form button
        pyautogui.press('tab')  # Focus on TP1_Name

        for value in testData:
            print "Setting", value  # , 'to', key
            if value == 'select':
                pyautogui.press('enter')
            else:
                pyautogui.typewrite(value)

            pyautogui.press('tab')

        # If correctly tabbed through, then focus should now be on Save button
        # Click Sign and Save button
        pyautogui.press('enter')

        self.driver.switch_to.window(self.driver.window_handles[-1])

    def sign_save_form(self):
        # This is just to call __set__(). Draws an image
        self.signaturePad = 'Sign'

        self.saveButton.click()
        time.sleep(3)
