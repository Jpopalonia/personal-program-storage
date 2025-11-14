# face driver code for momo cosplay

# TODO:
# make good

# module imports
import random
import time
import board
import digitalio
import displayio
import framebufferio
import terminalio
import rgbmatrix
import adafruit_imageload
import gifio

from adafruit_debouncer import Debouncer
from adafruit_led_animation.color import *

# release any previously initialized displays before running any code
displayio.release_displays()

# initialize the physical pixel matrix
matrix = rgbmatrix.RGBMatrix(
    width = 64,
    height = 64,
    bit_depth = 4,
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

# create tile map for each gif
face_grid = displayio.TileGrid(
    bitmap = face_gif.bitmap,
    pixel_shader = displayio.ColorConverter(
        input_colorspace = displayio.Colorspace.RGB565
    ))
face_gif.next_frame()

heart_grid = displayio.TileGrid(
    bitmap = heart_gif.bitmap,
    pixel_shader = displayio.ColorConverter(
        input_colorspace = displayio.Colorspace.RGB565
    ))
heart_gif.next_frame()

# define buttons
button_1_pin = digitalio.DigitalInOut(board.A2)
button_1_pin.direction = digitalio.Direction.INPUT
button_1_pin.pull = digitalio.Pull.UP
button_1 = Debouncer(button_1_pin)

button_2_pin = digitalio.DigitalInOut(board.A3)
button_2_pin.direction = digitalio.Direction.INPUT
button_2_pin.pull = digitalio.Pull.UP
button_2 = Debouncer(button_2_pin)

button_3_pin = digitalio.DigitalInOut(board.A4)
button_3_pin.direction = digitalio.Direction.INPUT
button_3_pin.pull = digitalio.Pull.UP
button_3 = Debouncer(button_3_pin)

button_4_pin = digitalio.DigitalInOut(board.A1)
button_4_pin.direction = digitalio.Direction.INPUT
button_4_pin.pull = digitalio.Pull.UP
button_4 = Debouncer(button_4_pin)

#<add background tilegrid here when ready>
main_group.append(face_grid)
display.refresh()

# function definitions

# updates displayed face gif
def change_face():
    pass

# advances the background by 1 frame
def update_background():
    pass

# advances the currently selected face by 1 frame
def update_face():
    pass

# main loop
while True:
    display.refresh()
    time.sleep(face_gif.next_frame())