#!/usr/bin/python
# -*- coding: utf-8 -*-

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
addrBitcoin = ''
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
with open('/home/pi/rPi_LCD_btcDisplay/addressBitcoin.txt') as f:
	arrayAddr = f.readlines()
#Number of elements the array
#
arrayAddrLen = len(arrayAddr)
i = 0
j = 0

while True:
	lcd.clear()
	lcd.backlight(lcd.BLUE)
	lcd.message('Getting New\nData from Blockr.io')

	addrBitcoin = arrayAddr[i]
	
	for j in range(3):
		try:
			btcURL = urllib2.urlopen(baseBitcoin + addrBitcoin)
		except Exception:
			lcd.clear()
			lcd.backlight(lcd.YELLOW)
			lcd.message('Working...')
			time.sleep(waitTimeSec)
			print(j)
		else:
			break
	else:
		lcd.clear()
		lcd.backlight(lcd.RED)
		lcd.message('Connectivity\nError')
		sys.exit()
	
	#btcURL = urllib2.urlopen(baseBitcoin + addrBitcoin)
	response = btcURL.read()
	responseDictionary = json.loads(response)
	lcd.clear()
	lcd.backlight(lcd.GREEN)
	
	if responseDictionary['status'] == 'success':
		bitcoinBalance = responseDictionary['data']['balance']
		if bitcoinBalance < minBtc:
			lcd.backlight(lcd.RED)
			lcd.message('Address Empty???\n' + addrBitcoin)
		else:
			lcd.message('btc: ' + str(bitcoinBalance) + '\n' + addrBitcoin)
		i = (i + 1)%int(arrayAddrLen)
	else:
		bitcoinBalance = 'Error \nCheck Internet'
		lcd.backlight(lcd.RED)
		lcd.message(bitcoinBalance)
	
	time.sleep(waitTimeSec)