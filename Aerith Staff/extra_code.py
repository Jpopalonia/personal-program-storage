# button A to change spell
# button B to cast spell

# program imports
import board
import digitalio
import neopixel
import time

# pin declarations
buttonAPin = board.D11
buttonAGndPin = board.D12
buttonBPin = board.D5
buttonBGndPin = board.D6

# import animations
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.blink import Blink

from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.color import *

# initialize button input
buttonA = digitalio.DigitalInOut(buttonAPin)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.UP

buttonAGnd = digitalio.DigitalInOut(buttonAGndPin)
buttonAGnd.direction = digitalio.Direction.OUTPUT
buttonAGnd.value = 0

buttonB = digitalio.DigitalInOut(buttonBPin)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.UP

buttonBGnd = digitalio.DigitalInOut(buttonBGndPin)
buttonBGnd.direction = digitalio.Direction.OUTPUT
buttonBGnd.value = 0

num_pixels = 26

# enable power to external Neopixels
ext_pwr = digitalio.DigitalInOut(board.EXTERNAL_POWER)
ext_pwr.direction = digitalio.Direction.OUTPUT
ext_pwr.value = 1

pixels = neopixel.NeoPixel(board.EXTERNAL_NEOPIXELS, num_pixels, brightness = 0.1, auto_write = False)

materia1 = PixelSubset(pixels, 0, 1)
materia2 = PixelSubset(pixels, 9, 10)

materia_anim = AnimationGroup(
  Solid(materia1, color = GREEN),
  Solid(materia2, color = YELLOW),
  sync = True
)

print("Ready!")

while True:
  materia_anim.animate()