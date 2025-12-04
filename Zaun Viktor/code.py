# pulses 2 LED n00ds on different phases to create an effect of fluid flowing through a tube

import time
import board
import pwmio
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

# maybe set max current to 50mA/0.05A?
aw.constant_current_range = 0.05

aw.set_constant_current(0, 255) # set pin1 to max current (approx 37mA according to the datasheet)
aw.set_constant_current(1, 255) # set pin2 to max current

# do these even support PWM? (probably not tbh)
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

    pin1.duty_cycle = PWM[value1]
    pin2.duty_cycle = PWM[value2]
    time.sleep(0.02)