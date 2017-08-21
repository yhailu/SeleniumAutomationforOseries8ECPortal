from selenium.webdriver.common.by import By
# Dictionary of locators
locators = {}

# login/logout
locators["login.username"] = [
    By.NAME,
    "username"]
locators["login.password"] = [By.NAME, "password"]
locators["login.submit.button"] = [By.XPATH, "login.submit.button"]
locators["login.login.link"] = [By.LINK_TEXT, "Log In"]
locators["login.logout.link"] = [By.LINK_TEXT, "Log Out"]
locators["login.login.button"] = [By.NAME, "create"]
locators["ECPLogoutPageTitle"] = "O Series Development Web"
locators["create.user.link"] = [
    By.LINK_TEXT, "Create New User"]


locators["create.new.customer"] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#accountInfo > fieldset > input#newCustomer']

# Input fields for create user acct.
locators['customer.status.continue'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#accountInfo > div.button-bar > input.button2']

locators['new.customer.companyName'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#companyName"]
locators['new.customer.email'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#companyEmail"]
locators['new.customer.userName'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#userName"]
locators['new.customer.password'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#password"]
locators['new.customer.confirmPassword'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#confirmPassword"]
locators['new.customer.personalEmail'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#personalEmail"]
locators['new.customer.firstName'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#firstName"]
locators['new.customer.lastName'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#lastName"]
locators['new.customer.phoneNumber'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#phoneNumber"]
locators['new.customer.countrySelect'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > div.countryStateSelect > select#country"]
locators['new.customer.street1'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#street1"]
locators['new.customer.street2'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#street2"]
locators['new.customer.city'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#city"]
locators['new.customer.stateSelect'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > div.countryStateSelect > select#state"]
locators['new.customer.postalCode'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#postalCode"]

# Security Questions
locators['new.customer.securityQuestions1'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > select#securityQuestions1"]
locators['new.customer.securityAnswer1'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#securityAnswer1"]
locators['new.customer.securityQuestions2'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > select#securityQuestions2"]
locators['new.customer.securityAnswer2'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#securityAnswer2"]
locators['new.customer.securityQuestions3'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > select#securityQuestions3"]
locators['new.customer.securityAnswer3'] = [
    By.CSS_SELECTOR,
    "div > div#main > div#column_right > form#accountInfo > div.showBorder > fieldset > input#securityAnswer3"]

# Existing Customer
locators['customer.code'] = [By.CSS_SELECTOR,
                             'div > div#main > div#column_right > form#accountInfo > fieldset > span > span#custCode > input#customerCode']
locators['existing.customer'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#accountInfo > fieldset > span > input#exsitingCustomer']

# create certificate
locators['create.certificate'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#cert > div.button-bar > input.button2']


locators['select.jurisdiction'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#certificateBean > div.column1of5 > span > label']
locators['select.jurisdiction.2'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#certificateBean > div.column2of5 > span > label']
locators['select.jurisdiction.3'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#certificateBean > div.column3of5 > span > label']
locators['select.jurisdiction.4'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#certificateBean > div.column4of5 > span > label']

# complete certificate
# search box
locators['search.box'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#cert > div#certificateManager > div#certificatesTable_wrapper.dataTables_wrapper > div.fg-toolbar.ui-toolbar.ui-widget-header.ui-corner-tl.ui-corner-tr.ui-helper-clearfix > div#certificatesTable_filter.dataTables_filter > label > input']
# search item found on first row of Certificate Manager table
locators['first.row.from.search'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#cert > div#certificateManager > div#certificatesTable_wrapper.dataTables_wrapper > div.dataTables_scroll > div.dataTables_scrollBody > table#certificatesTable.display.dataTable > tbody > tr.odd > td#certNumber']
locators['complete.button'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#cert > div.button-bar > input#complete.button2']

# renew certificate
locators['renew.button'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#cert > div.button-bar > input#renew.button2']

locators['continue'] = [
    By.ID, 'continue']

locators['certificate.form.dropdownlist'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#cert > fieldset >  select#form ']
locators['new.certificate.issue.date'] = [
    By.ID, 'coverages0.issueDate']
locators['new.certificate.issue.datepicker'] = [
    By.CSS_SELECTOR, 'div.ui-datepicker  > table.ui-datepicker-calendar > tbody > tr > td']
# initial pass doesnt implement expiration date
locators['new.certificate.expiration.date'] = [
    By.ID, 'coverages0.expirationDate']
locators['new.certificate.expiration.datepicker'] = [
    By.CSS_SELECTOR, 'div.ui-datepicker  > table.ui-datepicker-calendar > tbody > tr > td']

# Signature cavas
locators['certificate.signature'] = [
    By.CSS_SELECTOR,
    'div > div#main > div#column_right > form#signature > div#canvasDiv > canvas#canvas']

# Save button
locators['save'] = [
    By.ID, 'save']

"""renew certificate"""
locators['renew.certificate.expiration.date'] = [By.ID, 'expirationDate']
locators['renew.certificate.expiration.datepicker'] = [
    By.CSS_SELECTOR,
    'div.ui-datepicker > table.ui-datepicker-calendar > tbody > tr > td ']
