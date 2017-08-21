'''
Created on Mar 10, 2017

@author: Uma Pillai
'''

from BaseClasses.BasePageObject import BasePageObject


class ECPortalPageObject(BasePageObject):

    def __init__(self, driver):
        super(ECPortalPageObject, self).__init__(driver)
        self.driver = driver
