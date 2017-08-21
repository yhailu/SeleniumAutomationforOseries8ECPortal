'''
Created on Mar 10, 2017

@author: Uma Pillai
'''

from BaseClasses.BasePageObject import BasePageObject
from UIClasses.CustomElements import FormElement
from UIClasses.UIElements import TextBoxElement, ButtonElement, LinkElement,\
    RadioButtonElement, ListElement, DropDownListElement


# from Locators import locators
class CreatePortalPageObject(BasePageObject):
    compName = TextBoxElement('new.customer.companyName')
    compEmail = TextBoxElement('new.customer.email')
    uName = TextBoxElement('new.customer.userName')
    pWord = TextBoxElement('new.customer.password')
    cPassword = TextBoxElement('new.customer.confirmPassword')
    pEmail = TextBoxElement('new.customer.personalEmail')
    fName = TextBoxElement('new.customer.firstName')
    lName = TextBoxElement('new.customer.lastName')
    pNumber = TextBoxElement('new.customer.phoneNumber')
    cSelect = DropDownListElement('new.customer.countrySelect')
    Street1 = TextBoxElement('new.customer.street1')
    Street2 = TextBoxElement('new.customer.street2')
    City = TextBoxElement('new.customer.city')
    sSelect = DropDownListElement('new.customer.stateSelect')
    pCode = TextBoxElement('new.customer.postalCode')
    sq1Select = DropDownListElement('new.customer.securityQuestions1')
    sq1Answer = TextBoxElement('new.customer.securityAnswer1')
    sq2Select = DropDownListElement('new.customer.securityQuestions2')
    sq2Answer = TextBoxElement('new.customer.securityAnswer2')
    sq3Select = DropDownListElement('new.customer.securityQuestions3')
    sq3Answer = TextBoxElement('new.customer.securityAnswer3')
    continueButton = ButtonElement("customer.status.continue")
    # existing customer
    existingCustomerCode = TextBoxElement('customer.code')

    def __init__(self, driver):
        super(CreatePortalPageObject, self).__init__(driver)
        createUserLink = LinkElement("create.user.link")
        createUserLink.click()

    def setup_new_customer(self, companyName, companyEmail, userName, password, confirmPassword, personalEmail,
                           firstName, lastName, phoneNumber, countrySelect, street1, street2, city, stateSelect, postalCode, securityQuestion1,
                           securityQuestion1Answer,
                           securityQuestion2,
                           securityQuestion2Answer,
                           securityQuestion3,
                           securityQuestion3Answer):

        print 'setup_new_customer'
        createNewCustomer = RadioButtonElement("create.new.customer")
        createNewCustomer.select()

        self.continueButton.click()

        self.compName = companyName
        self.compEmail = companyEmail
        self.uName = userName
        self.pWord = password
        self.cPassword = confirmPassword
        self.pEmail = personalEmail
        self.fName = firstName
        self.lName = lastName
        self.pNumber = phoneNumber
        self.cSelect = countrySelect
        self.Street1 = street1
        self.Street2 = street2
        self.City = city
        self.sSelect = stateSelect
        self.pCode = postalCode
        self.sq1Select = securityQuestion1
        self.sq1Answer = securityQuestion1Answer
        self.sq2Select = securityQuestion2
        self.sq2Answer = securityQuestion2Answer
        self.sq3Select = securityQuestion3
        self.sq3Answer = securityQuestion3Answer
        self.continueButton.click()

    def edit_existing_customer(self, customerCode, companyEmail, userName, password, confirmPassword, personalEmail,
                               firstName, lastName, phoneNumber, countrySelect, street1, street2, city, stateSelect, postalCode, securityQuestion1,
                               securityQuestion1Answer,
                               securityQuestion2,
                               securityQuestion2Answer,
                               securityQuestion3,
                               securityQuestion3Answer):

        print 'edit_existing_customer'
        existingCustomerRadio = RadioButtonElement("existing.customer")
        existingCustomerRadio.select()
        self.existingCustomerCode = customerCode
        self.continueButton.click()
        self.compEmail = companyEmail
        self.uName = userName
        self.pWord = password
        self.cPassword = confirmPassword
        self.pEmail = personalEmail
        self.fName = firstName
        self.lName = lastName
        self.pNumber = phoneNumber
        self.cSelect = countrySelect
        self.Street1 = street1
        self.Street2 = street2
        self.City = city
        self.sSelect = stateSelect
        self.pCode = postalCode
        self.sq1Select = securityQuestion1
        self.sq1Answer = securityQuestion1Answer
        self.sq2Select = securityQuestion2
        self.sq2Answer = securityQuestion2Answer
        self.sq3Select = securityQuestion3
        self.sq3Answer = securityQuestion3Answer
        self.continueButton.click()
