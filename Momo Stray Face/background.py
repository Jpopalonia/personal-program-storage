import time
import board
import digitalio
import displayio
import framebufferio
import rgbmatrix
import gifio

import touchio
import adafruit_debouncer

import adafruit_fancyled.adafruit_fancyled as fancy
from adafruit_led_animation.color import *

# release any previously initialized displays before running any code
displayio.release_displays()

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

matrix = rgbmatrix.RGBMatrix(
  width=64, height=64, bit_depth=3,
  rgb_pins=[board.MTX_R1, board.MTX_G1, board.MTX_B1, board.MTX_R2, board.MTX_G2, board.MTX_B2],
  addr_pins=[board.MTX_ADDRA, board.MTX_ADDRB, board.MTX_ADDRC, board.MTX_ADDRD, board.MTX_ADDRE],
  clock_pin=board.MTX_CLK, latch_pin=board.MTX_LAT, output_enable_pin=board.MTX_OE)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

# background colors
bg_colors = [
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  BLUE,
  PURPLE
]

num_colors = len(bg_colors)

bitmap = displayio.Bitmap(display.width, display.height, num_colors)
palette = displayio.Palette(num_colors)

# add into the for loop below to adjust brightness
# not necessary for a 64x64 with reduced bit depth and proper diffusion
#colors[i] = fancy.normalize(colors[i])
#colors[i] = fancy.gamma_adjust(colors[i], brightness=0.5)
#colors[i] = fancy.denormalize(colors[i])

for i in range(num_colors):
  palette[i] = bg_colors[i]

background_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
main_group = displayio.Group()

main_group.append(background_grid)
display.root_group = main_group

# global variable initialization
curr_color = 0
prev_start = 0
old_time = 0
curr_time = 0

touch_pin1 = board.A1

touch1 = touchio.TouchIn(touch_pin1)

# updates the background
def update_background(start_value):
  for y in range(bitmap.height):
    curr_color = y + start_value
    for x in range(bitmap.width):
      bitmap[x, y] = curr_color % num_colors
      curr_color += 1
  display.refresh()

# main loop
while True:
  curr_time = time.monotonic()
  if curr_time - old_time > 0.75:
    old_time = curr_time
    update_background(prev_start)
    prev_start += 1 # tracks the background color to animate it correctly
  elif touch1.value:
    led.value = 1
  else:
    led.value = 0