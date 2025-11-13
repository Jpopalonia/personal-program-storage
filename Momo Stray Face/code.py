# face driver code for momo cosplay

# TODO:
# make good

# module imports
import random
import time
import board
import displayio
import framebufferio
import terminalio
import rgbmatrix
import adafruit_imageload
import gifio
import sys

import adafruit_fancyled.adafruit_fancyled as fancy
from adafruit_led_animation.color import *

from adafruit_display_text import label

# release any previously initialized displays before running any code
displayio.release_displays()

# initialize the physical pixel matrix
matrix = rgbmatrix.RGBMatrix(
    width = 64,
    height = 64,
    bit_depth = 3,
    rgb_pins = [board.MTX_R1,
                board.MTX_G1,
                board.MTX_B1,
                board.MTX_R2,
                board.MTX_G2,
                board.MTX_B2],
    addr_pins = [board.MTX_ADDRA,
                 board.MTX_ADDRB,
                 board.MTX_ADDRC,
                 board.MTX_ADDRD,
                 board.MTX_ADDRE],
    clock_pin = board.MTX_CLK,
    latch_pin = board.MTX_LAT,
    output_enable_pin = board.MTX_OE)

# initialize the virtual framebuffer display
display = framebufferio.FramebufferDisplay(
    framebuffer = matrix,
    auto_refresh = False)
display.refresh()
main_group = displayio.Group()
display.root_group = main_group

# load images into memory
face_gif = gifio.OnDiskGif('images/face.gif')
heart_image, heart_palette = adafruit_imageload.load(
    file_or_filename = 'images/heart.gif',
    bitmap = displayio.Bitmap,
    palette = displayio.Palette)
heart_palette.make_transparent(0)
heart_gif = gifio.OnDiskGif('images/heart.gif')

# initialization of variables for background
colors = [
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    PURPLE]

current_background_color = 0

# create tile map for foreground
foreground = displayio.TileGrid(
    bitmap = heart_gif.bitmap,
    pixel_shader = heart_palette)

# add background tilegrid here when ready
main_group.append(foreground)
display.refresh()

# function definitions

# takes in an image palette and desired brightness, returns the adjusted palette
def adjust_brightness(input_palette, desired_brightness):
    pass

# advances the background by 1 frame
def update_background():
    pass

# main loop
while True:
    time.sleep(1)