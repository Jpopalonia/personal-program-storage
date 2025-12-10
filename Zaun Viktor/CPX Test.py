# pulses 2 sets of neopixels to allow for testing with CPX

import time
import board
import pwmio
import random
import neopixel

from adafruit_simplemath import map_range

from adafruit_led_animation.color import *
from adafruit_led_animation.helper import PixelSubset

import pwm_lightness
PWM = pwm_lightness.get_pwm_table(0xffff, max_input=255) # precalculate gamma corrected values

pixels = neopixel.NeoPixel(
    pin = board.NEOPIXEL,
    n = 10,
    brightness = 0.1,
    auto_write = False)

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

pin1.fill(PINK)
pin2.fill(PINK)

pixels.show()

increasing1 = True
increasing2 = True

value1 = 0
value2 = 240

speed = 1

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
        value1 += speed
    if increasing2:
        value2 += speed
    if not increasing1:
        value1 -= speed
    if not increasing2:
        value2 -= speed

    brightness1 = map_range(x = PWM[value1],
                                in_min = 0,
                                in_max = 65535,
                                out_min = 0,
                                out_max = 1)
    brightness2 = map_range(x = PWM[value2],
                                in_min = 0,
                                in_max = 65535,
                                out_min = 0,
                                out_max = 1)
    
    new_color1 = list(PINK)
    new_color2 = list(PINK)

    for elem in new_color1:
        elem *= brightness1
    
    for elem in new_color2:
        elem *= brightness2

    new_color1 = tuple(new_color1)
    new_color2 = tuple(new_color2)

    print(new_color1)
    print(new_color2)

    pin1.fill(new_color1)
    pin2.fill(new_color2)

    pixels.show()

    time.sleep(0.02)