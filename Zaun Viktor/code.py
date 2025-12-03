# pulses 2 LED n00ds on different phases to create an effect of fluid flowing through a tube

import time
import board
import pwmio

import pwm_lightness
PWM = pwm_lightness.get_pwm_table(0xffff, max_input=255) # precalculate gamma corrected values

pin1 = pwmio.PWMOut(board.D3)
pin2 = pwmio.PWMOut(board.D4)

increasing1 = True
increasing2 = True

value1 = 90
value2 = 230

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