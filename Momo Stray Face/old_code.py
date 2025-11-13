# stray companion display code
# features:
# -scrolling rainbow background
# -animated expressions on top (palette color 0 will be transparent)

# TODO:
# -code is terrible due to scope creep, needs refactoring
# -include gifio for animation
# -break apart background and foreground animation timers

import random
import time
import board
import displayio
import framebufferio
import terminalio
import rgbmatrix
import adafruit_imageload
import gifio

import adafruit_fancyled.adafruit_fancyled as fancy
from adafruit_led_animation.color import *

from adafruit_display_text import label

# release any previously initialized displays before running any code
displayio.release_displays()

matrix = rgbmatrix.RGBMatrix(
  width=32, height=16, bit_depth=6,
  rgb_pins=[board.MTX_R1, board.MTX_G1, board.MTX_B1, board.MTX_R2, board.MTX_G2, board.MTX_B2],
  addr_pins=[board.MTX_ADDRA, board.MTX_ADDRB, board.MTX_ADDRC],
  clock_pin=board.MTX_CLK, latch_pin=board.MTX_LAT, output_enable_pin=board.MTX_OE)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

colors = [
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  BLUE,
  PURPLE
]

display.refresh()

# create a bitmap to display a heart animation on top of the background
heart1_bitmap, heart1_palette = adafruit_imageload.load("/heart1.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
heart1_grid = displayio.TileGrid(heart1_bitmap, pixel_shader=heart1_palette)

heart1_color = []

for i in range(len(heart1_palette)):
  heart1_color.append(heart1_palette[i])
  heart1_color[i] = fancy.unpack(heart1_color[i])
  heart1_color[i] = fancy.gamma_adjust(heart1_color[i], brightness=0.25)
  heart1_color[i] = fancy.denormalize(heart1_color[i])
  heart1_palette[i] = heart1_color[i]

heart1_palette.make_transparent(0)

heart2_bitmap, heart2_palette = adafruit_imageload.load("/heart2.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
heart2_grid = displayio.TileGrid(heart2_bitmap, pixel_shader=heart2_palette)

heart2_color = []

for i in range(len(heart2_palette)):
  heart2_color.append(heart2_palette[i])
  heart2_color[i] = fancy.unpack(heart2_color[i])
  heart2_color[i] = fancy.gamma_adjust(heart2_color[i], brightness=0.25)
  heart2_color[i] = fancy.denormalize(heart2_color[i])
  heart2_palette[i] = heart2_color[i]

heart2_palette.make_transparent(0)

# load a bitmap to display a facial expression on top of the background
face_bitmap, face_palette = adafruit_imageload.load("/neutral.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
face_grid = displayio.TileGrid(face_bitmap, pixel_shader=face_palette)

face_color = []

for i in range(len(face_palette)):
  face_color.append(face_palette[i])
  face_color[i] = fancy.unpack(face_color[i])
  face_color[i] = fancy.gamma_adjust(face_color[i], brightness=0.25)
  face_color[i] = fancy.denormalize(face_color[i])
  face_palette[i] = face_color[i]

face_palette.make_transparent(0)
num_colors = len(colors)

bitmap = displayio.Bitmap(display.width, display.height, num_colors)
palette = displayio.Palette(num_colors)

for i in range(num_colors):
  colors[i] = fancy.normalize(colors[i])
  colors[i] = fancy.gamma_adjust(colors[i], brightness=0.25)
  colors[i] = fancy.denormalize(colors[i])
  palette[i] = colors[i]

curr_color = 0
prev_start = 0

background_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
main_group = displayio.Group()

main_group.append(background_grid)
main_group.append(heart1_grid)

old_time = 0
curr_time = 0
anim_frame = 1

while True:
  curr_time = time.monotonic()
  if curr_time - old_time > 0.5:
    old_time = curr_time
    display.refresh()
    time.sleep(0.5)
    main_group.remove(heart1_grid)
    main_group.append(heart2_grid)
    display.refresh()
    time.sleep(0.5)
    main_group.remove(heart2_grid)
    main_group.append(heart1_grid)
    display.refresh()
    display.root_group = main_group
    for y in range(bitmap.height):
      curr_color = y + prev_start
      for x in range(bitmap.width):
        bitmap[x, y] = curr_color % num_colors
        curr_color += 1
    prev_start += 1
  else:
    pass