#! /usr/bin/env python
'''
    Andrew Baumann's contribution to David Brizan's
    doctoral thesis project. All code is under the
    GNU License

    Special thanks to this:
    https://wiki.python.org/moin/SimplePrograms
'''
import glob

class Streamy: 
    def __init__(self, q):
        self.query = q
        self.processed = glob.glob('*.txt')

    def Picker(self):
        for file_name in sorted(self.processed):
            print ('    ------' + file_name)

            with open(file_name) as f:
                for line in f:
                    if line.find(self.query) != -1:
                        print ('    ' + line.rstrip())

            print
