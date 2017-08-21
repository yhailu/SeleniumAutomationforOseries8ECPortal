'''
Created on Mar 14, 2017

@author: Uma Pillai
'''
import csv


class csvLibrary(object):

    def read_csv_file(self, filename):
        '''Read CSV file and return content as a Python list.
        '''

        f = open(filename, 'r')
        csvfile = csv.reader(f)
        f.close
        return [row for row in csvfile]

    def empty_csv_file(self, filename):
        '''Empty (truncate) the CSV file.
        '''

        f = open(filename, "w")
        f.truncate()
        f.close()

    def append_list_to_csv_file(self, filename, data):
        '''Append data to new or existing CSV file.
        Data should be iterable (e.g. list or tuple)
        '''

        f = open(filename, 'ab')
        csvfile = csv.writer(f)
        for item in data:
            csvfile.writerow([item])
        f.close()

    def append_to_csv_file(self, filename, data):
        '''Append single row of data to new or existing CSV file.
        '''
        f = open(filename, 'ab')
        csvfile = csv.writer(f)
        csvfile.writerow(data)
        f.close()
