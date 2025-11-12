# aerith staff prop

# TODO:
# improve animations for spells

import time
import board
import digitalio
import neopixel

from adafruit_debouncer import Debouncer

from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.pulse import Pulse

from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup

from adafruit_led_animation.color import *

# pin definitions
pixel_pin = board.NEOPIXEL
button1_pin = board.BUTTON
button2_pin = board.EXTERNAL_BUTTON

# button 1 initialization
button1_config = digitalio.DigitalInOut(button1_pin)
button1_config.direction = digitalio.Direction.INPUT
button1_config.pull = digitalio.Pull.UP

button1 = Debouncer(button1_config)

# button 2 initialization
button2_config = digitalio.DigitalInOut(button2_pin)
button2_config.direction = digitalio.Direction.INPUT
button2_config.pull = digitalio.Pull.UP

button2 = Debouncer(button2_config)

# enable external power output
ext_pwr = digitalio.DigitalInOut(board.EXTERNAL_POWER)
ext_pwr.direction = digitalio.Direction.OUTPUT
ext_pwr.value = True

# neopixel initialization
num_pixels = 18
pixel_brightness = 1

materia_pixels = neopixel.NeoPixel(pin = board.NEOPIXEL,
                                   n = 1,
                                   brightness = 0.5,
                                   pixel_order = neopixel.GRB)

staff_pixels = neopixel.NeoPixel(pin = board.EXTERNAL_NEOPIXELS,
                                 n = 1,
                                 brightness = 0.05,
                                 pixel_order = neopixel.RGB)

# global variable initialization
current_spell = 0

# animation initializations
idle_update_speed = 0.1
idle_breath_duration = 0.5
idle_breath_period = 3

# spell animations
firaga = Blink(pixel_object = staff_pixels,
               speed = 0.5,
               color = RED)

blizzaga = Blink(pixel_object = staff_pixels,
                 speed = 0.5,
                 color = BLUE)

curaga = Blink(pixel_object = staff_pixels,
               speed = 0.5,
               color = GREEN)

thundaga = Blink(pixel_object = staff_pixels,
                 speed = 0.5,
                 color = YELLOW)

# materia idle animations
firaga_materia_idle = Pulse(pixel_object = materia_pixels,
                            speed = idle_update_speed,
                            color = RED,
                            period = idle_breath_period,
                            breath = idle_breath_duration)

blizzaga_materia_idle = Pulse(pixel_object = materia_pixels,
                            speed = idle_update_speed,
                            color = BLUE,
                            period = idle_breath_period,
                            breath = idle_breath_duration)

curaga_materia_idle = Pulse(pixel_object = materia_pixels,
                            speed = idle_update_speed,
                            color = GREEN,
                            period = idle_breath_period,
                            breath = idle_breath_duration)

thundaga_materia_idle = Pulse(pixel_object = materia_pixels,
                            speed = idle_update_speed,
                            color = YELLOW,
                            period = idle_breath_period,
                            breath = idle_breath_duration)

# materia casting animations
firaga_materia_active = Solid(pixel_object = materia_pixels,
                              color = RED)

blizzaga_materia_active = Solid(pixel_object = materia_pixels,
                                color = BLUE)

curaga_materia_active = Solid(pixel_object = materia_pixels,
                              color = GREEN)

thundaga_materia_active = Solid(pixel_object = materia_pixels,
                                color = YELLOW)

# function definitions
def change_spell():
    global current_spell

    current_spell += 1

    if current_spell > 3:
        current_spell = 0

def cast_spell():
    global current_spell
    now = time.monotonic()

    if current_spell == 0:
        firaga_materia_active.animate()
        while time.monotonic() - now < 5:
            firaga.animate()
    elif current_spell == 1:
        blizzaga_materia_active.animate()
        while time.monotonic() - now < 5:
            blizzaga.animate()
    elif current_spell == 2:
        curaga_materia_active.animate()
        while time.monotonic() - now < 5:
            curaga.animate()
    elif current_spell == 3:
        thundaga_materia_active.animate()
        while time.monotonic() - now < 5:
            thundaga.animate()
    
    staff_pixels.fill(0)
    staff_pixels.show()

# main loop
while True:
    button1.update()
    button2.update()

    if button1.fell:
        change_spell()
    elif button2.fell:
        cast_spell()
    
    if current_spell == 0:
        firaga_materia_idle.animate()
    elif current_spell == 1:
        blizzaga_materia_idle.animate()
    elif current_spell == 2:
        curaga_materia_idle.animate()
    elif current_spell == 3:
        thundaga_materia_idle.animate()
