#! /usr/bin/env python
'''
    Andrew Baumann's contribution to David Brizan's
    doctoral thesis project. All code is under the
    GNU License

    Special thanks to this:
    https://wiki.python.org/moin/SimplePrograms
'''

class Utterance:
    def __init__(sent, speak, ty):
        self.sentence = sent
        self.speaker = speak 
        self.typee = ty 
    