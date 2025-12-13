# pulses 2 LED n00ds on different phases to create an effect of fluid flowing through a tube

# TODO:
# test with calculate_intensity() method from adafruit_led_animation

import time
import board
import pwmio
import random
import neopixel

from adafruit_simplemath import map_range

from adafruit_led_animation.helper import PixelSubset

from adafruit_led_animation.color import *

import pwm_lightness
PWM = pwm_lightness.get_pwm_table(0xffff, max_input=255) # precalculate gamma corrected values

pixels = neopixel.NeoPixel(
    pin = board.NEOPIXEL,
    n = 10,
    brightness = 1,
    auto_write = False
)

pin1 = PixelSubset(
    pixel_object = pixels,
    start = 0,
    end = 5
)

pin2 = PixelSubset(
    pixel_object = pixels,
    start = 5,
    end = 10
)

increasing1 = True
increasing2 = True

value1 = random.randint(90, 230)
value2 = random.randint(90, 230)

while True:
    if value1 >= 255:
        increasing1 = False
    if value2 >= 255:
        increasing2 = False
    if value1 <= 32:
        increasing1 = True
    if value2 <= 32:
        increasing2 = True
    
    if increasing1:
        value1 += random.random(1, 5)
    if increasing2:
        value2 += random.random(1, 5)
    if not increasing1:
        value1 -= random.random(1, 5)
    if not increasing2:
        value2 -= random.random(1, 5)

    # map pwm values to normalized values here
    adj_value1 = map_range(
        x = PWM[value1],
        in_min = 0,
        in_max = 255,
        out_min = 0,
        out_max = 1
    )

    adj_value2 = map_range(
        x = PWM[value2],
        in_min = 0,
        in_max = 255,
        out_min = 0,
        out_max = 1
    )

    pin1.fill(adj_value1)
    pin2.fill(adj_value2)

    pin1.show()
    pin2.show()