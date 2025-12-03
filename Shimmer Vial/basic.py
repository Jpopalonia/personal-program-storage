# turn on and show a static color on neopixel jewel (7 LEDs)

import time
import board
import neopixel

color = 0x6E22CD

pixels = neopixel.NeoPixel(board.D2, 7, brightness = 1, auto_write = False, pixel_order = neopixel.GRBW)

pixels.fill(0x6E22CD)
pixels.show()

while True:
  pass