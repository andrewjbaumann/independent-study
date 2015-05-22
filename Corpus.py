#! /usr/bin/env python
'''
    Andrew Baumann's contribution to David Brizan's
    doctoral thesis project. All code is under the
    GNU License

    Special thanks to this:
    https://wiki.python.org/moin/SimplePrograms
'''

class Corpus:
    def __init__(self, corp, type_of_disflu):
        self.corpii = corp
        self.diflu = type_of_disflu