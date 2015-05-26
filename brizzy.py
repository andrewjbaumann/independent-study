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
from Corpus import Corpus

x = ""
y = ""

while True:
	x = input("what are you searching for? ")
	if x == "D" or x == "d":
		x = "{D"
		break
	elif x == "F" or x == "f":
		x = "{F"
		break
	elif x == "C" or x == "c":
		x = "{C"
		break
	elif x == "E" or x == "e":
		x = "{E"
		break
	elif x == "repeat":
		x = "+"
		break

while True:
	y = input("which corpus do you want to look in? ")
	if y ==  "Switchboard" or y == "sw":
		y = "sw"
		run = Corpus(x, y)
		run.Start()
		break
	else: 
		continue 








