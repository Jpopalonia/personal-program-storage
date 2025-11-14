import time
import board
import digitalio
import adafruit_imageload
import displayio
import rgbmatrix
import framebufferio

from adafruit_debouncer import Debouncer

# release any previously initialized displays before running any code
displayio.release_displays()

# initialize the physical pixel matrix
matrix = rgbmatrix.RGBMatrix(
    width = 64,
    height = 64,
    bit_depth = 4,
    rgb_pins = [board.MTX_R1,
                board.MTX_G1,
                board.MTX_B1,
                board.MTX_R2,
                board.MTX_G2,
                board.MTX_B2],
    addr_pins = [board.MTX_ADDRA,
                 board.MTX_ADDRB,
                 board.MTX_ADDRC,
                 board.MTX_ADDRD,
                 board.MTX_ADDRE],
    clock_pin = board.MTX_CLK,
    latch_pin = board.MTX_LAT,
    output_enable_pin = board.MTX_OE)

# initialize the virtual framebuffer display
display = framebufferio.FramebufferDisplay(
    framebuffer = matrix,
    auto_refresh = False)
display.refresh()
main_group = displayio.Group()
display.root_group = main_group

# load test images
img_1 = displayio.OnDiskBitmap('images/1.bmp')
img_2 = displayio.OnDiskBitmap('images/2.bmp')
img_3 = displayio.OnDiskBitmap('images/3.bmp')
img_4 = displayio.OnDiskBitmap('images/4.bmp')

# create tilegrids for each image
img_1_grid = displayio.TileGrid(
    bitmap = img_1,
    pixel_shader = img_1.pixel_shader
)

img_2_grid = displayio.TileGrid(
    bitmap = img_2,
    pixel_shader = img_2.pixel_shader
)

img_3_grid = displayio.TileGrid(
    bitmap = img_3,
    pixel_shader = img_3.pixel_shader
)

img_4_grid = displayio.TileGrid(
    bitmap = img_4,
    pixel_shader = img_4.pixel_shader
)

# define buttons
button_1_pin = digitalio.DigitalInOut(board.A2)
button_1_pin.direction = digitalio.Direction.INPUT
button_1_pin.pull = digitalio.Pull.UP
button_1 = Debouncer(button_1_pin)

button_2_pin = digitalio.DigitalInOut(board.A3)
button_2_pin.direction = digitalio.Direction.INPUT
button_2_pin.pull = digitalio.Pull.UP
button_2 = Debouncer(button_2_pin)

button_3_pin = digitalio.DigitalInOut(board.A4)
button_3_pin.direction = digitalio.Direction.INPUT
button_3_pin.pull = digitalio.Pull.UP
button_3 = Debouncer(button_3_pin)

button_4_pin = digitalio.DigitalInOut(board.A1)
button_4_pin.direction = digitalio.Direction.INPUT
button_4_pin.pull = digitalio.Pull.UP
button_4 = Debouncer(button_4_pin)

while True:
    button_1.update()
    button_2.update()
    button_3.update()
    button_4.update()

    if(not button_1.value):
        print("Pressed 1")
    if(not button_2.value):
        print("Pressed 2")
    if(not button_3.value):
        print("Pressed 3")
    if(not button_4.value):
        print("Pressed 4")

    time.sleep(0.1)