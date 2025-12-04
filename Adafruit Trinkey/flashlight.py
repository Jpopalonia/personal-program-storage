# program for Adafruit Trinkey
# shows white on all LEDs, brightness changes on touching either pad

# TODO:
# potentially add gamma correction with fancyled or manually calculated gamma

import time
import board
import touchio
import neopixel

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=False, brightness = 0.05)

pixels.fill(0xFFFFFF)
pixels.show()

touched = time.monotonic()

while True:
  if time.monotonic() - touched < 0.15:
    continue
  if touch1.value:
    # Touch pad 1 to increase the brightness.
    pixels.brightness += 0.05
    pixels.show()
    touched = time.monotonic()
  elif touch2.value:
    # Touch pad 2 to decrease the brightness.
    pixels.brightness -= 0.05
    pixels.show()

    touched = time.monotonic()
