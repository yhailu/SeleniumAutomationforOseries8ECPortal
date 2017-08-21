'''
Created on Apr 14, 2017

@author: Uma Pillai
'''

from BaseClasses.BasePageElement import BasePageElement, highlight
from UIClasses.UIElements import RadioButtonElement, DateElement, LinkElement
from UIClasses.UIElements import TextBoxElement, ListElement, CheckBoxElement

from ElementUtilities import findElement, getAbsoluteXPath
from ElementUtilities import getElementAttributes


class FormElement (BasePageElement):

    def __init__(self, locator):
        super(FormElement, self).__init__(locator)

    def __get__(self, obj, val):
        self.formElements = []
        parent = findElement(self.findBy, self.locator)
        highlight(parent)

        elements = parent.find_elements_by_xpath(".//*")

        for element in elements:
            absPath = getAbsoluteXPath(element)
            try:
                dynamicEle = DynamicElement(absPath)
                if dynamicEle:
                    self.formElements.append(dynamicEle)
            except:
                pass
        return self.formElements

    def __set__(self, obj, val):
        pass


class DynamicElement(BasePageElement):

    def __init__(self, locator):
        super(DynamicElement, self).__init__(locator)
        self.locator = locator

    def __new__(cls, locator):
        from Locators import locators
        findBy = 'xpath'
        locators.update({'dynamicElement': [findBy, str(locator)]})
#         print locators['dynamicElement']
        element = findElement(findBy, locator)

#         highlight(element)
#         attributes = getElementAttributes(element)
#         print (
#             "-attrib:",
#             attributes,
#             element.tag_name,
#             element.get_attribute('href'),
#             element.text)
        elementType = element.get_attribute('type')
        elementClass = element.get_attribute('class')

        if element.tag_name == 'input':
            if elementType == 'text':
                #                 highlight(element)
                if element.get_attribute('placeholder') == 'MM/DD/YYYY':
                    return DateElement("dynamicElement")
                else:
                    return TextBoxElement("dynamicElement")

        if element.tag_name == 'a':
            #             highlight(element)
            return LinkElement("dynamicElement")

        if element.tag_name == 'text-area':
            #             highlight(element)
            return TextBoxElement("dynamicElement")

        if element.tag_name == 'select':
            #             highlight(element)
            return ListElement("dynamicElement")

        if elementClass == 'input-group':
            #             highlight(element)
            controls = element.find_elements_by_xpath(".//*")

            for control in controls:
                controlClass = control.get_attribute('class')
                if controlClass in ['radio', 'checkbox']:
                    locator = getAbsoluteXPath(element)
                    locators.update({'dynamicElement': [findBy, str(locator)]})

                    return (RadioButtonElement("dynamicElement") if (
                        controlClass == 'radio') else CheckBoxElement("dynamicElement"))
