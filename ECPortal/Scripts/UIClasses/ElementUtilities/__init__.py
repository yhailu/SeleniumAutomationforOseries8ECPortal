from BaseClasses import selenium_driver
from selenium.webdriver.support.select import Select
from BaseClasses.BasePageElement import NoSuchElementException


def findElement(findBy, locator):
    driver = selenium_driver.driver
    element = None

    try:
        element = driver.find_element(findBy, locator)
    except:
        raise NoSuchElementException(findBy, locator)

    if element:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    return element


def findSelectElement(findBy, locator):
    driver = selenium_driver.driver
    try:
        select = Select(driver.find_element(findBy, locator))
    except:
        raise NoSuchElementException(locator)

    return select


def findElements(findBy, locator):
    driver = selenium_driver.driver
    try:
        element = driver.find_elements(findBy, locator)
    except:
        raise NoSuchElementException(locator)

    return element


def findElementsInGroup(findBy, parentlocator):
    driver = selenium_driver.driver
    parent = driver.find_element(findBy, parentlocator)
    try:
        #         element = parent.find_elements(findBy, ".//*")
        element = parent.find_elements(findBy, ".//label")
    except:
        raise NoSuchElementException(parentlocator)

    return element


def getElementAttributes(element):
    driver = selenium_driver.driver
    attr = driver.execute_script('''
        var items = {};
        for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value };
        return items;''', element)
    return attr


def getAbsoluteXPath(element):
    driver = selenium_driver.driver
    absPath = driver.execute_script(
        "function absoluteXPath(element) {" +
        "var comp, comps = [];" +
        "var parent = null;" +
        "var xpath = '';" +
        "var getPos = function(element) {" +
        "var position = 1, curNode;" +
        "if (element.nodeType == Node.ATTRIBUTE_NODE) {" +
        "return null;" +
        "}" +
        "for (curNode = element.previousSibling; curNode; curNode = curNode.previousSibling){" +
        "if (curNode.nodeName == element.nodeName) {" +
        "++position;" +
        "}" +
        "}" +
        "return position;" +
        "};" +

        "if (element instanceof Document) {" +
        "return '/';" +
        "}" +

        "for (; element && !(element instanceof Document); element = element.nodeType == Node.ATTRIBUTE_NODE ? element.ownerElement : element.parentNode) {" +
        "comp = comps[comps.length] = {};" +
        "switch (element.nodeType) {" +
        "case Node.TEXT_NODE:" +
        "comp.name = 'text()';" +
        "break;" +
        "case Node.ATTRIBUTE_NODE:" +
        "comp.name = '@' + element.nodeName;" +
        "break;" +
        "case Node.PROCESSING_INSTRUCTION_NODE:" +
        "comp.name = 'processing-instruction()';" +
        "break;" +
        "case Node.COMMENT_NODE:" +
        "comp.name = 'comment()';" +
        "break;" +
        "case Node.ELEMENT_NODE:" +
        "comp.name = element.nodeName;" +
        "break;" +
        "}" +
        "comp.position = getPos(element);" +
        "}" +

        "for (var i = comps.length - 1; i >= 0; i--) {" +
        "comp = comps[i];" +
        "xpath += '/' + comp.name.toLowerCase();" +
        "if (comp.position !== null) {" +
        "xpath += '[' + comp.position + ']';" +
        "}" +
        "}" +

        "return xpath;" +
        "}" +
        "return absoluteXPath(arguments[0]);", element)

    return absPath
