# stray game companion display code
# features:
# -scrolling rainbow background
# -animated expressions on top (palette color 0 will be transparent)

# TODO:
# -code is terrible due to scope creep, needs refactoring
# -include gifio for animation
# -break apart background and foreground animation timers

# library imports
import time
import board
import displayio
import gifio
import framebufferio
import rgbmatrix
import adafruit_imageload

import adafruit_fancyled.adafruit_fancyled as fancy
from adafruit_led_animation.color import *

# release any previously initialized displays before running any code
displayio.release_displays()

# brightness options
loading_brightness = 0.25
face_brightness = 0.25
bg_brightness = 0.25

# timing options (seconds per cycle)
bg_interval = 0.75
anim_interval = 0.5

# colors for background in display order (RGB tuple or from adafruit_led_animation.color)
bg_colors = [
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  BLUE,
  PURPLE
]

# initialize RGBMatrix and assign as displayio object (3 address lines for 32x16 matrix)
matrix = rgbmatrix.RGBMatrix(
  width=32, height=16, bit_depth=6,
  rgb_pins=[board.MTX_R1, board.MTX_G1, board.MTX_B1, board.MTX_R2, board.MTX_G2, board.MTX_B2],
  addr_pins=[board.MTX_ADDRA, board.MTX_ADDRB, board.MTX_ADDRC], # add pins here for larger displays
  clock_pin=board.MTX_CLK, latch_pin=board.MTX_LAT, output_enable_pin=board.MTX_OE)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

# create and display a loading screen while initializing
'''loading_screen, loading_palette = adafruit_imageload.load("/clock.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
loading_grid = displayio.TileGrid(loading_screen, pixel_shader=loading_palette)
loading_group = displayio.Group()
loading_group.append(loading_grid)
display.root_group = loading_group # push load screen to display

# set brightness of loading screen
loading_color = []
for i in range(len(loading_palette)):
  loading_color.append(loading_palette[i])
  loading_color[i] = fancy.unpack(loading_color[i])
  loading_color[i] = fancy.gamma_adjust(loading_color[i], brightness=loading_brightness)
  loading_color[i] = fancy.denormalize(loading_color[i])
  loading_palette[i] = loading_color[i]'''

display.refresh()
# end of load screen routine

# function definitions
def drawBackground():
  for y in range(bg_bitmap.height):
      curr_color = y + prev_start
      for x in range(bg_bitmap.width):
        bg_bitmap[x, y] = curr_color % len(bg_palette)
        curr_color += 1

# create background objects
bg_bitmap = displayio.Bitmap(display.width, display.height, len(bg_colors))
bg_palette = displayio.Palette(len(bg_colors))

# globals for main loop
curr_bg_time = 0
old_bg_time = 0
curr_anim_time = 0
old_anim_time = 0
anim_frame = 0
prev_start = 0

# main loop
while True:
  if curr_bg_time - old_bg_time > bg_interval:
    prev_start += 1
  if curr_anim_time - old_anim_time > anim_interval:
    anim_frame += 1