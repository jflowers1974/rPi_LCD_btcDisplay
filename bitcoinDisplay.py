#!/usr/bin/python
# -*- coding: utf-8 -*-

import textwrap
import sys
import urllib2

#Make certain that the permission permit writing to
#
sys.path.append("/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
#
lcd = Adafruit_CharLCDPlate()

