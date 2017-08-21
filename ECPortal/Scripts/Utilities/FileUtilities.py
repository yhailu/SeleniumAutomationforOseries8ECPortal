'''
Created on May 8, 2017

@author: Uma Pillai
'''


class FileUtilities(object):

    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def convertPDF2HTML(self, pdf_content):
        cmd = 'python %PYTHONPATH%\Scripts\pdf2txt.py -t html "' + \
            pdf_content + '"'
        print cmd

        from subprocess import Popen, PIPE
        ps = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = ps.communicate(input=pdf_content)
        if ps.returncode != 0:
            raise OSError(ps.returncode, cmd, stderr)

        return stdout

    def cleanHTML(self, html_content):
        import re
        clean_html = re.compile('<.*?>')
        html_content = re.sub(clean_html, '', html_content)

        html_content = self.removeDates(html_content)

        return html_content

    def removeDates(self, html_content):
        import re

        date_pattern = re.compile(r'\d{4}[-/]\d{2}[-/]\d{2}')
#         dateF = date_pattern.findall(html_content)
#         print "before", dateF

#         html_content = re.sub(r'\d{4}[-/]\d{2}[-/]\d{2}', '', html_content)
        html_content = re.sub(date_pattern, '', html_content)

#         dateF = date_pattern.findall(html_content)
#         print "after", dateF

        return html_content
