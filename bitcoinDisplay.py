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
waitTimeSec = 5
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
#and input into an array
#
with open('addressBitcoin.txt') as f:
	arrayAddr = []
	for line in f:
		arrayAddr.append(line)
#Number of elements the array
#
arrayAddrLen = len(arrayAddr) + 1
i=0
while True:
	if i > arrayAddrLen:
		i = 0
	else:
		lcd.clear()
		lcd.backlight(lcd.GREEN)
		lcd.message('Getting New\nData from Blockr.io')
	
		addrBitcoin = arrayAddr[i]
		btcAPI = urllib2.urlopen(baseBitcoin + addrBitcoin)
		response = btcAPI.read()
		responseDictionary = json.loads(response)
	
		if responseDictionary['status'] == 'success':
			bitcoinBalance = responseDictionary['data']['balance']
			if bitcoinBalance < minBtc:
				lcd.backlight(lcd.RED)
				lcd.message(addrBitcoin + '\nCheck MT')
			else:
				lcd.message(addrBitcoin + '\nContains:' + str(bitcoinBalance))
				print addrBitcoin
				print str(bitcoinBalance)
				print i
				time.sleep(waitTimeSec)
				i = i + 1
		else:
			bitcoinBalance = 'Err - Check Internet'
			lcd.backlight(lcd.RED)
			lcd.message(bitcoinBalance)
			time.sleep(waitTimeSec)

