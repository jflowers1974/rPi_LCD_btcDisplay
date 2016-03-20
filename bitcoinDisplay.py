#!/usr/bin/python
# -*- coding: utf-8 -*-

import textwrap
import json
import sys
import urllib2
import time

#Variables that can be adjusted
#per the user
#
minBtc = 0.01
waitTimeSec = 120
baseBitcoin = 'https://btc.blockr.io/api/v1/address/info/'
addrBitcoin = '198aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi'

#Make certain that the permission permit writing to
#
sys.path.append("/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
#
lcd = Adafruit_CharLCDPlate()

#Read the bitcoin addresses from external file
#first determine how many addresses there are
#Important to end the file on an Address
#
totalNumAddr=0
#Not the most eff, but gets the job done
#
with open('addressBitcoin.txt') as f:
	totalNumAddr = sum(1 for _ in f)


#Testing to see if I can just get one address
#
btcAPI = urllib2.urlopen(baseBitcoin + addrBitcoin)
response = btcAPI.read()
responseDictionary = json.loads(response)
if responseDictionary['status'] == 'success':
	bitcoinBalance = responseDictionary['data']['balance']
else:
	bitcoinBalance = 'Err - Check Internet'
