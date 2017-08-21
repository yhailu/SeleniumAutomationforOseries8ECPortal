'''
Created on Mar 10, 2017

@author: Yesusera and Uma
'''
from BaseClasses.BasePageTest import BasePageTest
from Pages import ECPortalPageObject, CreatePortalPageObject, CertificatePageObject
from Pages import LoginPageObject
import datetime


class ECP_keywords(BasePageTest):

    def construct_URL(self, host, port, portalTag, ws='/vertex-ec/'):
        url = ''.join(('http://', host, ':', port, ws, portalTag))
        return url

    def launch_URL(self, url, browser):
        super(ECP_keywords, self)._setUp_Test(url, browser)
        self.ecp = ECPortalPageObject.ECPortalPageObject(
            self.driver)
        self.ecp.launchURL(url)

    def login_with_username_and_password(self, username, password):
        print "Login with username and password-", username, password
        self.lpo = LoginPageObject.LoginPageObject(
            self.driver)

        self.lpo.login(username, password)

    def logout(self):
        print "Log Out"
        self.lpo.logout()

    def close_browser(self):
        super(ECP_keywords, self)._tearDown_Test()

    def create_portal_account(self, createFlag, customerCode, companyName, companyEmail, userName, password, confirmPassword, personalEmail,
                              firstName, lastName, phoneNumber, countrySelect, street1, street2, city, stateSelect, postalCode,
                              securityQuestion1, securityQuestion1Answer, securityQuestion2, securityQuestion2Answer,
                              securityQuestion3, securityQuestion3Answer):
        print "Create Portal Account"
        self.cpo = CreatePortalPageObject.CreatePortalPageObject(
            self.driver)

        if createFlag == 'True':
            self.cpo.setup_new_customer(
                companyName,
                companyEmail,
                userName,
                password,
                confirmPassword,
                personalEmail,
                firstName,
                lastName,
                phoneNumber,
                countrySelect,
                street1,
                street2,
                city,
                stateSelect,
                postalCode,
                securityQuestion1,
                securityQuestion1Answer,
                securityQuestion2,
                securityQuestion2Answer,
                securityQuestion3,
                securityQuestion3Answer)
        else:
            self.cpo.edit_existing_customer(customerCode,
                                            companyEmail, userName,
                                            password,
                                            confirmPassword,
                                            personalEmail,
                                            firstName,
                                            lastName,
                                            phoneNumber,
                                            countrySelect,
                                            street1,
                                            street2,
                                            city,
                                            stateSelect,
                                            postalCode,
                                            securityQuestion1,
                                            securityQuestion1Answer,
                                            securityQuestion2,
                                            securityQuestion2Answer,
                                            securityQuestion3,
                                            securityQuestion3Answer)

    def create_new_certificate(
            self, jurisdiction, form, issueDate='', expirationDate=''):
        # Expiration date set to be implemented
        if not issueDate:
            todayDate = datetime.date.today()
            issueDate = datetime.date(todayDate.year, todayDate.month, 1)
            issueDate = datetime.datetime.strftime(
                issueDate,
                '%m/%d/%Y')

        print "Create New Certificate-", jurisdiction, form, issueDate, expirationDate
        self.certificatePO = CertificatePageObject.CertificatePageObject(
            self.driver)

        self.certificatePO.create_newCertificate(
            jurisdiction,
            form,
            issueDate,
            expirationDate)

    def complete_certificate(self, certSearchString):
        print "Complete Certificate-", certSearchString
        self.certificatePO = CertificatePageObject.CertificatePageObject(
            self.driver)
        self.certificatePO.complete_certificate(
            certSearchString)

    def renew_certificate(self, certSearchString, expirationDate=''):
        # Set expiration date to 1 month after a year later
        if not expirationDate:
            todayDate = datetime.date.today()
            expirationDate = datetime.date(
                todayDate.year + 1,
                (todayDate.month % 12 + 1),
                15)
            expirationDate = datetime.datetime.strftime(
                expirationDate,
                '%m/%d/%Y')

        print "Renew Certificate-", certSearchString, expirationDate
        self.certificatePO = CertificatePageObject.CertificatePageObject(
            self.driver)
        self.certificatePO.renew_certificate(certSearchString,
                                             expirationDate)

    def fill_pdf_form(self, csvFilePath):
        print "Fill PDF form-", csvFilePath
        self.certificatePO.fill_pdf_form(csvFilePath)

    def sign_and_save_form(self):
        print "Sign and Save Form"
        self.certificatePO.sign_save_form()
