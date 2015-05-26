#! /usr/bin/env python
'''
    Andrew Baumann's contribution to David Brizan's
    doctoral thesis project. All code is under the
    GNU License

    Special thanks to this:
    https://wiki.python.org/moin/SimplePrograms
'''

class Utterance:
    def __init__(self, sentence, speaker, typ, file_name):
        self.sentence = sentence
        self.speaker = speaker
        self.typee = typ 
        self.file_name = file_name
    