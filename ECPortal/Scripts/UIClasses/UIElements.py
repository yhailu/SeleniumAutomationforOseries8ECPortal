'''
Created on Mar 15, 2017

@author: Uma Pillai
'''

from BaseClasses import selenium_driver
from BaseClasses.BasePageElement import BasePageElement
from BaseClasses.BasePageElement import highlight

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ElementUtilities import findElement, findElements, findSelectElement


# from ElementUtilities import findElementsInGroup, getElementAttributes
class TextBoxElement(BasePageElement):

    def __get__(self, obj, val):
        textBox = findElement(self.findBy, self.locator)

        highlight(textBox)
        val = textBox.get_attribute("value")
        return val

    def __set__(self, obj, val):
        textBox = findElement(self.findBy, self.locator)

        highlight(textBox)
        textBox.clear()
        textBox.send_keys(val)


class ButtonElement(BasePageElement):

    def __get__(self, obj, val):
        button = findElement(self.findBy, self.locator)

        highlight(button)
        return button

    def click(self):
        button = findElement(self.findBy, self.locator)

        highlight(button)
        button.click()
#         selenium_driver.driver.implicitly_wait(10)


class ListElement(BasePageElement):

    def __get__(self, obj, val):
        select = findSelectElement(self.findBy, self.locator)

        val = select.options
        return val

    def __set__(self, obj, val):
        select = findSelectElement(self.findBy, self.locator)

        val = val.strip()
        select.select_by_visible_text(val)

    def select(self):
        option = findElement(self.findBy, self.locator)

        highlight(option)
        option.click()


class CheckBoxElement(BasePageElement):

    def __get__(self, obj, val):
        options = findElements(self.findBy, self.locator)

        return options

    def __set__(self, obj, val):
        options = findElements(self.findBy, self.locator)

        val = val.strip()
        for option in options:
            if option.text.strip() == val:
                highlight(option)
                option.click()
                break

    def is_checked(self, option):
        # TODO
        pass

    def select(self):
        option = findElement(self.findBy, self.locator)

        highlight(option)
        option.click()

    def click(self):
        button = findElement(self.findBy, self.locator)

        highlight(button)
        button.click()


class DropDownListElement(BasePageElement):

    def __get__(self, obj, val):
        select = findSelectElement(self.findBy, self.locator)

        val = select.options
        return val

    def __set__(self, obj, val):
        select = findSelectElement(self.findBy, self.locator)

        val = val.strip()
        select.select_by_visible_text(val)

    def select(self):
        option = findElement(self.findBy, self.locator)

        highlight(option)
        option.click()


class RadioButtonElement(BasePageElement):

    def __get__(self, obj, val):
        options = findElements(self.findBy, self.locator)

        for option in options:
            highlight(option)

        return options

    def __set__(self, obj, val):
        options = findElements(self.findBy, self.locator)

        val = val.strip()
        for option in options:
            highlight(option)
#             option.click()
            if (val in option.text) or (val == option.text.strip()):
                option.click()
                break

    def select(self):
        option = findElement(self.findBy, self.locator)

        highlight(option)
        option.click()


class LinkElement (BasePageElement):

    def __init__(self, locator):
        super(LinkElement, self).__init__(locator)

    def __get__(self, obj, val):
        link = findElement(self.findBy, self.locator)

        highlight(link)
        self.linkText = link.text
        self.href = link.get_attribute('href')

        return link

    def click(self):
        link = findElement(self.findBy, self.locator)

        highlight(link)
        self.linkText = link.text
        self.href = link.get_attribute('href')

        link.click()

    def downloadAs(self, filetype, saveAsPrefix, saveFolder):
        link = findElement(self.findBy, self.locator)

        highlight(link)
        self.linkText = link.text
        self.href = link.get_attribute('href')

        import os

        self.linkText = self.linkText.replace('/', '_')
        self.linkText = self.linkText.strip()

        outFileName = saveAsPrefix + "_" + self.linkText + filetype
        outFileName = os.path.join(os.getcwd(), saveFolder, outFileName)
#         print self.href, self.linkText, outFileName

        import urllib
        urllib.urlretrieve(self.href, outFileName)

        return outFileName


class DateElement(BasePageElement):

    def __get__(self, obj, val):
        dateElement = findElement(self.findBy, self.locator)

        highlight(dateElement)
        dateElement.click()

        return dateElement.get_attribute("value")

    def __set__(self, obj, val):
        dateElement = findElement(self.findBy, self.locator)

        highlight(dateElement)

        from selenium.webdriver.common.keys import Keys
        dateElement.send_keys(Keys.SHIFT + Keys.HOME)
        dateElement.send_keys(val.replace('/', ''))

#         driver.execute_script('''
#                 var elem = arguments[0];
#                 var value = arguments[1];
#                 elem.value = value;''', dateElement, val)
#         dateElement.click()


class DatePickerElement(BasePageElement):

    def __get__(self, obj, val):
        pass

    def __set__(self, obj, val):
        dd = int(val.split("/")[1])
        print dd

        days = findElements(self.findBy, self.locator)

        for day in days:
            #             highlight(day)
            if day.text.strip() == str(dd):
                highlight(day)
                day.click()
                break


class LabelElement(BasePageElement):

    def __get__(self, obj, val):
        labelElement = findElement(self.findBy, self.locator)

        highlight(labelElement)
        return labelElement.text

    def click(self):
        link = findElement(self.findBy, self.locator)

        highlight(link)
        self.linkText = link.text
        self.href = link.get_attribute('href')

        link.click()


class CanvasElement(BasePageElement):

    def __set__(self, obj, val):
        driver = selenium_driver.driver
        canvasElement = findElement(self.findBy, self.locator)

        highlight(canvasElement)
        from selenium.webdriver.common.action_chains import ActionChains

        drawing = ActionChains(driver)\
            .click_and_hold(canvasElement)\
            .move_by_offset(-25, -50)\
            .move_by_offset(-25, 50)\
            .move_by_offset(75, -36)\
            .move_by_offset(-100, 0)\
            .move_by_offset(75, 36)\
            .release()

        drawing.perform()
