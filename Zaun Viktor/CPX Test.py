# pulses 2 LED n00ds on different phases to create an effect of fluid flowing through a tube

# TODO:
# test with calculate_intensity() method from adafruit_led_animation

import time
import board
import pwmio
import random
import neopixel

from adafruit_fancyled.adafruit_fancyled import normalize

from adafruit_simplemath import constrain

from adafruit_led_animation.helper import PixelSubset

from adafruit_led_animation.color import *

#import pwm_lightness
#PWM = pwm_lightness.get_pwm_table(0xffff, max_input=255) # precalculate gamma corrected values

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

increasing1 = False
increasing2 = True

lower_start = 90
upper_start = 230

lower_limit = 5
upper_limit = 255

value1 = random.randint(lower_start, upper_start)
value2 = random.randint(lower_start, upper_start)

while True:
    if value1 >= upper_limit:
        increasing1 = False
    if value2 >= upper_limit:
        increasing2 = False
    if value1 <= lower_limit:
        increasing1 = True
    if value2 <= lower_limit:
        increasing2 = True
    
    if increasing1:
        value1 += random.randint(1, 5)
    if increasing2:
        value2 += random.randint(1, 5)
    if not increasing1:
        value1 -= random.randint(1, 5)
    if not increasing2:
        value2 -= random.randint(1, 5)

    value1 = constrain(value1, 0, 255)
    value2 = constrain(value2, 0, 255)

    # map pwm values to normalized values here
    adj_value1 = normalize(value1)
    adj_value2 = normalize(value2)

    color1 = calculate_intensity(PINK, adj_value1)
    color2 = calculate_intensity(PINK, adj_value2)

    pin1.fill(color1)
    pin2.fill(color2)

    pixels.show()
    time.sleep(0.05)