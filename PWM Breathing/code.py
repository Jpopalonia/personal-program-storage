import time, board, pwmio, pwm_lightness
PWM = pwm_lightness.get_pwm_table(0xffff, max_input=255)
output_pin = pwmio.PWMOut(board.A1)
while True:
    for v in range(255, -1, -1):
        output_pin.duty_cycle = PWM[v]
        time.sleep(0.01)
    for v in range(1, 255):
        output_pin.duty_cycle = PWM[v]
        time.sleep(0.01)