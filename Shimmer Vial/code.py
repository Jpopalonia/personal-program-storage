# show a pulsing animation

import time
import board
import neopixel

color = 0x6E22CD

pixels = neopixel.NeoPixel(board.D2, 7, brightness = 1, auto_write = False, pixel_order = neopixel.GRBW)

curr_brightness = 0
increasing = True
pixels.fill(color)
pixels.show()

# simple breathing animation
while True:
  if increasing and curr_brightness < 1:
    curr_brightness += 0.01
    pixels.brightness = curr_brightness
    pixels.show()
  elif not increasing and curr_brightness > 0.05:
    curr_brightness -= 0.01
    pixels.brightness = curr_brightness
    pixels.show()
  else:
    increasing = not increasing
  time.sleep(0.07)