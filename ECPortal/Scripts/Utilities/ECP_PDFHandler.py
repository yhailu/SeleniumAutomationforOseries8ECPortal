'''
Created on Jul 16, 2017

@author: Uma Pillai
'''

from cStringIO import StringIO

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1


class PDFElement(object):

    def __init__(self, name, value, coordinates):
        '''
        Constructor
        '''
        self.name = name
        self.value = value
        self.coordinates = coordinates

    def __repr__(self):
        return ('<name=%s;value=%s;coordinates=%s>' %
                (self.name, self.value, self.coordinates))


class PDFHandler(object):
    '''
    WIP - Class to handle the PDF interactions for ECPortal application
    Uses pdfminer
    '''

    def __init__(self, url, cookies={}):
        '''
        Constructor
        '''
        import requests
        print 'cookies', cookies
        self.request = requests.get(url, cookies=cookies)

        memory_file = StringIO(self.request.content)

        # Create a PDF parser object associated with the StringIO object
        parser = PDFParser(memory_file)

        # Create a PDF document object that stores the document structure
        self.document = PDFDocument(parser)

    def resolve_pdf(self):

        pdfStructure = []

        fields = resolve1(self.document.catalog['AcroForm'])['Fields']

        for i in fields:
            field = resolve1(i)
            name, value, bbox = field.get(
                'T'), field.get('V'), field.get('Rect')
#             print '{0}: {1}: {2}: {3}'.format(name, value, bbox, s)

            pdfElement = PDFElement(name, value, bbox)
            print pdfElement

            pdfStructure.append(pdfElement)

        return pdfStructure
