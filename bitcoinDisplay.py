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
minBtc = 0.001
waitTimeSec = 5
baseBitcoin = 'https://btc.blockr.io/api/v1/address/info/'
addrBitcoin = '1EJYcY9VHu8A1YrijJzr8ponGSByWxsugb'
#Make certain that the permission permit writing to
#
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate')
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
#
lcd = Adafruit_CharLCDPlate()

#Read the bitcoin addresses from external file
#and input into an array
#
arrayAddr = []
with open('addressBitcoin.txt') as f:
	arrayAddr = f.readlines()
#Number of elements the array
#
arrayAddrLen = len(arrayAddr)
i=0

while True:
	lcd.clear()
	lcd.backlight(lcd.GREEN)
	lcd.message('Getting New\nData from Blockr.io')

	addrBitcoin = arrayAddr[i]
	btcAPI = urllib2.urlopen(baseBitcoin + addrBitcoin)
	response = btcAPI.read()
	responseDictionary = json.loads(response)
	lcd.clear()
	
	if responseDictionary['status'] == 'success':
		bitcoinBalance = responseDictionary['data']['balance']
		if bitcoinBalance < minBtc:
			lcd.backlight(lcd.RED)
			lcd.message('Address Empty???\n' + addrBitcoin)
		else:
			print(bitcoinBalance)
			print(addrBitcoin)
			lcd.message('btc: ' + str(bitcoinBalance) + '\n' + addrBitcoin)
		i = (i + 1)%int(arrayAddrLen)
	else:
		bitcoinBalance = 'Error \nCheck Internet'
		lcd.backlight(lcd.RED)
		lcd.message(bitcoinBalance)
	
	time.sleep(waitTimeSec)