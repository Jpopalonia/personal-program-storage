# The circuit contains 1 button that is used to swap between each mode
# Modes: Prismatic White, Spectrum Cycling, Rave Mode

import board
import digitalio
import neopixel

import time
import random

from rainbowio import colorwheel
from adafruit_debouncer import Debouncer

from adafruit_led_animation.color import *

# pin definitions
led_pin = board.LED
pixel_pin = board.D5
button_pin = board.D9

# speed options
# increase to speed up, decrease to slow down
prismatic_speed = 35
spectrum_speed = 20
rave_bpm = 174
light_interval = 50
dark_interval = 50

# led setup
led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT

# button setup
button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

switch = Debouncer(button)

# neopixel setup
num_pixels = 12
pixel_brightness = 1
subpixel_order = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin,
                           num_pixels,
                           brightness = pixel_brightness,
                           auto_write = False,
                           pixel_order = subpixel_order)

# global variable initialization
mode = 0
color_pos = 0
prev_elem = None
curr_elem = None
prev_time = 0    

rave_colors = [WHITE, 
               RED, 
               GREEN, 
               BLUE, 
               YELLOW, 
               CYAN, 
               PURPLE]

if(pixels.byteorder == neopixel.RGBW or pixels.byteorder == neopixel.GRBW):
    rave_colors[0] = RGBW_WHITE_W

# constant definitions
BILLION = 10 ** 9
rave_bpm /= 60

random.seed(time.time())

# function definitions

# rainbow vomit cycling, averages to white
def prismatic_cycle(color):
    for pixel in range(num_pixels):
        pixel_index = (pixel * 256 // num_pixels) + color * 5
        pixels[pixel] = colorwheel(pixel_index & 255)

# spectrum cycling, all pixels get the same color
def spectrum_cycle(color):
    set_color = colorwheel(color)
    for i in range(num_pixels):
        pixels[i] = set_color

# rapidly flashes a random color at a given tempo
def rave_mode():
    global prev_elem
    global curr_elem

    while curr_elem == prev_elem:
        curr_elem = random.choice(rave_colors)
    prev_elem = curr_elem

    for i in range(num_pixels):
        pixels[i] = curr_elem

def light_mode():
    pixels.fill(WHITE)

def dark_mode():
    pixels.fill(BLACK)

def change_mode():
    global mode
    mode += 1

    if mode >= 5:
        mode = 0

led.value = False

# main loop
while True:
    now = time.monotonic_ns() / BILLION

    # read button state
    switch.update()

    # increment mode on button press
    if switch.fell:
        change_mode()
        prev_time = now
    
    if mode == 0 and (now - prev_time) > (1 / prismatic_speed):
        prismatic_cycle(color_pos)
        color_pos += 1
        prev_time = now
    elif mode == 1 and (now - prev_time) > (1 / spectrum_speed):
        spectrum_cycle(color_pos)
        color_pos += 1
        prev_time = now
    elif mode == 2 and (now - prev_time) > (1 / rave_bpm):
        rave_mode()
        prev_time = now
    elif mode == 3 and (now - prev_time) > (1 / light_interval):
        light_mode()
    elif mode == 4 and (now - prev_time) > (1 / dark_interval):
        dark_mode()
    
    pixels.show()