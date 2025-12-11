# program to drive the LEDs and other devices in a full-body Warwick cosplay

# TODO:
# make

# program imports
import board
import time
import random
import neopixel
import digitalio

# animation lib imports
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.comet import Comet

# animation helper imports
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup

# color constant imports
from adafruit_led_animation.color import *

# neopixel options and initialization
neo_pin = board.NEOPIXEL
num_pixels = 10
neo_brightness = 1

pixels = neopixel.NeoPixel(
    pin = neo_pin,
    n = num_pixels,
    brightness = neo_brightness,
    auto_write = False
)

# animation options and initialization
comet_speed = 0.1
comet_color = BLACK
comet_bg_color = GREEN
comet_tail_length = 10

tube_animation = Comet(
    pixel_object = pixels,
    speed = comet_speed,
    color = comet_color,
    background_color = comet_bg_color,
    tail_length = comet_tail_length
)

# global variable initialization
rippy_dippy = True # placeholder

# function definitions
def butts(): # placeholder
    return 'my butt'

# main loop
while True:
    tube_animation.animate()