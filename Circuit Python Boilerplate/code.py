# boilerplate program for creating new CircuitPython programs

# TODO:
# make

# project imports
import time
import board
import random
import neopixel
import digitalio

import supervisor

# initialize built-in LED
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output(value = False)

# show whether USB is connected
if supervisor.runtime.usb_connected:
  led.value = True   # USB
else:
  led.value = False  # no USB

# pin definitions

# global variable initialization

# function definitions

# main loop
while True:
    pass