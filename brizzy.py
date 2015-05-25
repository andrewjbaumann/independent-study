#! /usr/bin/env python
'''
	Andrew Baumann's contribution to David Brizan's
	doctoral thesis project. All code is under the
	GNU License

	Special thanks to this:
	https://wiki.python.org/moin/SimplePrograms
'''

import glob
from Streamy import Streamy 
from Corpus import Corpus
from Utterance import Utterance

x = ""
y = ""

while True:
	x = input("what are you searching for? ")
	if x == "D" or x == "d":
		x = "{D"
		break
	else if x == "F" or x == "f";
		x = "{F"
		break
	else if x == "C" or x == "c";
		x = "{C"
		break
	else if x == "E" or x == "e";
		x = "{E"
		break
	else if x == "repeat"
		x = "+"
		break

while True:
	y = input("which corpus do you want to look in? ")
	if y ==  "Switchboard" or y == "sw":
		run = Streamy(x, "sw")
		run.Picker()
		break
	else: 
		continue 








