# pulses 2 LED n00ds on different phases to create an effect of fluid flowing through a tube
# this version uses the aw9523 led driver board over i2c

import time
import board
import adafruit_aw9523

import pwm_lightness

# precalculate gamma corrected values
PWM = pwm_lightness.get_pwm_table(0xffff, max_input=255) # look into this and re-learn how it works

# may need fixed once i can get my hands on a board for testing
i2c = board.I2C()
aw = adafruit_aw9523.AW9523(i2c)

# set all pins to output and LED (constant current) mode
aw.LED_modes = 0xFFFF
aw.directions = 0xFFFF

# does this mean 0.05A?
aw.constant_current_range = 0.05

aw.set_constant_current(0, 255) # set pin1 to max current (approx 37mA according to the datasheet I think)
aw.set_constant_current(1, 255) # set pin2 to max current

# external driver board pins
pin1 = aw.get_pin(0)
pin2 = aw.get_pin(1)

increasing1 = True
increasing2 = True

value1 = 90
value2 = 230

# main loop (elaborate on how this works, maybe roll up some functions from this)
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
        value1 += 1
    if increasing2:
        value2 += 1
    if not increasing1:
        value1 -= 1
    if not increasing2:
        value2 -= 1

    # pin 1 set current
    # pin 2 set current
    time.sleep(0.02)