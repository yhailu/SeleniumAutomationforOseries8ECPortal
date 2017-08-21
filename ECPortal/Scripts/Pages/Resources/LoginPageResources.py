'''
Created on Mar 29, 2017

@author: Uma Pillai
'''

from UIClasses.UIElements import TextBoxElement, ButtonElement, LinkElement


class LoginPageResources(object):

    '''
    classdocs
    '''
    username = TextBoxElement("login.username")
    password = TextBoxElement("login.password")
    submitButton = ButtonElement("login.submit.button")
    loginLink = LinkElement("login.login.link")
    logoutLink = LinkElement("login.logout.link")
