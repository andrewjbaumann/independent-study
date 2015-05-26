#! /usr/bin/env python
'''
    Andrew Baumann's contribution to David Brizan's
    doctoral thesis project. All code is under the
    GNU License

    Special thanks to this:
    https://wiki.python.org/moin/SimplePrograms
'''
import glob
import os
from Utterance import Utterance

class Streamy: 
    def __init__(self, query, corpii):
        self.query = query
        self.corp = corpii
        self.file_list = set()
        self.utt_list = set()
        self.write_file = open("new.txt", 'w')
        if corpii == "sw":
            self.processed = glob.glob('corpus/switchboard/*/*.utt')

    def picker(self):
        for file_name in sorted(self.processed):
            #print ('    ------' + file_name)

            with open(file_name) as f:
                for line in f:
                    if line.find(self.query) != -1:
                        utt = Utterance(line, "", self.query, file_name)
                        self.utt_list.add(utt)
                        self.file_list.add(file_name)

        temp = list(sorted(self.file_list))
        for file_name in temp:
            self.write_file.write("%s\n" % file_name)

        self.write_file.close()


