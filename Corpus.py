#! /usr/bin/env python
'''
    Andrew Baumann's contribution to David Brizan's
    doctoral thesis project. All code is under the
    GNU License

    Special thanks to this:
    https://wiki.python.org/moin/SimplePrograms
'''
from Utterance import Utterance
from Streamy import Streamy 

class Corpus:
    def __init__(self, corp, type_of_disflu):
        self.corpii = corp
        self.diflu = type_of_disflu

    def Start(self):
    	x = Streamy(self.corpii, self.diflu)
    	x.picker()