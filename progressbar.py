#!/usr/bin/python
# -*- coding: utf-8 -*-

# Martin Rybensky 2018-10-03

# 
# SIMPLE PYTHON PROGRESSBAR
#

import sys
import time

# progressbar function's parameters:

# done - int value, the amount which is already done
# total - int value, the amount of the whole
# style - int value, visual style of the progress bar, see below

# style = 1  |█████████████████████████████████████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░| 73%
# style = 2  [=========================================================================---------------------------] 73%
# style = 3  [#########################################################################...........................] 73%

def progressbar(done,total,style):

	totalpct = float(total) / 100
	if done == 0:
		donepct = 0
	else:
		donepct = float(done) / totalpct
		donepct = round(donepct)
		donepct = int(donepct)

	zbyva = 100 - donepct
	hotovo = donepct

	if style == 1:
		bar = "|" + opakuj_znak(u'\u2588',hotovo) + opakuj_znak(u'\u2591',zbyva) + "|"
	elif style == 2:
		bar = "[" + opakuj_znak('=',hotovo) + opakuj_znak('-',zbyva) + "]"
	elif style == 3:
		bar = "[" + opakuj_znak('#',hotovo) + opakuj_znak('.',zbyva) + "]"

	sys.stdout.write("\r" + bar + " " + str(donepct) + "% (" + str(done) + "/" + str(total) +")")
	sys.stdout.flush()


def opakuj_znak(znak,pocet):
	return (znak * ((pocet/len(znak))+1))[:pocet]


########################################################################################################################
# feature demonstration
#
# [user@pc]$ chmod u+x progressbar.py
# [user@pc]$ ./progressbar.py
#

style = 1

for x in range(0,30):
	progressbar(x,30,style)
	time.sleep(1)

print "\n"
sys.exit(0)
