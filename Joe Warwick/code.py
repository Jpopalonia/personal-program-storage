# program to drive the LEDs and other devices in a full-body Warwick cosplay

# TODO:
# wtf board am I gonna use?
# how the heck am I gonna hook everything up? probably just 1 pin per each
# control either over IR or BTLE!?!
# clean up unused imports (they take a lot of memory)

# parts list:
# right gauntlet
# left gauntlet
# left shoulder
# left forearm
# right elbow
# right oblique
# eyes?
# back of neck
# back tank
# belly?

# program imports
import board
import time
import random
import neopixel
import digitalio

# animation lib imports
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.rainbowcomet import RainbowComet

# animation helper imports
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup

# color constant imports
from adafruit_led_animation.color import *

# neopixel settings and initialization
neo_pin = board.NEOPIXEL
num_pixels = 10
neo_brightness = 0.1

pixels = neopixel.NeoPixel(
    pin = neo_pin,
    n = num_pixels,
    brightness = neo_brightness,
    auto_write = False
)

# animation settings and initialization
comet_speed = 0.2
comet_color = GREEN
comet_bg_color = BLACK
comet_tail_length = 13

tube_animation = Comet(
    pixel_object = pixels,
    speed = comet_speed,
    color = comet_color,
    background_color = comet_bg_color,
    tail_length = comet_tail_length,
    ring = True
)

# global variable initialization
rippy_dippy = True # placeholder

# function definitions
def butts(): # placeholder
    return 'my butt'

# main loop
while True:
    tube_animation.animate()