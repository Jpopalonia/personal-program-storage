# face driver code for momo cosplay

# TODO:
# make good

# Notes:
# black is treated as transparent within the foreground gifs

# module imports
import time
import board
import adafruit_debouncer
import digitalio
import displayio
import framebufferio
import rgbmatrix
import gifio

from adafruit_led_animation.color import *

# release any previously initialized displays before running any code
displayio.release_displays()

# initialize the physical pixel matrix
matrix = rgbmatrix.RGBMatrix(
    width = 64,
    height = 64,
    bit_depth = 2,
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

# initialize the display framebuffer
display = framebufferio.FramebufferDisplay(
    framebuffer = matrix,
    rotation = 0,
    auto_refresh = False)
display.refresh()
main_group = displayio.Group()
display.root_group = main_group

# load images into memory
gifs = []

face_gif = gifio.OnDiskGif('images/face.gif')
gifs.append(face_gif)
heart_gif = gifio.OnDiskGif('images/heart.gif')
gifs.append(heart_gif)

# initialization of variables for background
background_colors = [
    RED,
    ORANGE,
    YELLOW,
    GREEN,
    BLUE,
    PURPLE]

background_palette = displayio.Palette(
    color_count = len(background_colors)
)

for i in range(len(background_colors)):
    background_palette[i] = background_colors[i]

current_background_color = 0
bg_color_start = 0
current_face = 0

# create tile map for each gif
tile_grids = []

face_grid = displayio.TileGrid(
    bitmap = face_gif.bitmap,
    pixel_shader = displayio.ColorConverter(
        input_colorspace = displayio.Colorspace.RGB565
    ))

# black is treated as transparent
face_grid.pixel_shader.make_transparent(0x000000) 
tile_grids.append(face_grid)

heart_grid = displayio.TileGrid(
    bitmap = heart_gif.bitmap,
    pixel_shader = displayio.ColorConverter(
        input_colorspace = displayio.Colorspace.RGB565
    ))

# black is treated as transparent
heart_grid.pixel_shader.make_transparent(0x000000)
tile_grids.append(heart_grid)

# background tile grid
background_bitmap = displayio.Bitmap(
    display.width,
    display.height,
    len(background_colors))

background_grid = displayio.TileGrid(
    bitmap = background_bitmap,
    pixel_shader = background_palette)

# define buttons
buttons = []

button_0_pin = digitalio.DigitalInOut(board.A2)
button_0_pin.direction = digitalio.Direction.INPUT
button_0_pin.pull = digitalio.Pull.UP
button_0 = adafruit_debouncer.Button(button_0_pin)
buttons.append(button_0)

button_1_pin = digitalio.DigitalInOut(board.A3)
button_1_pin.direction = digitalio.Direction.INPUT
button_1_pin.pull = digitalio.Pull.UP
button_1 = adafruit_debouncer.Button(button_1_pin)
buttons.append(button_1)

button_2_pin = digitalio.DigitalInOut(board.A4)
button_2_pin.direction = digitalio.Direction.INPUT
button_2_pin.pull = digitalio.Pull.UP
button_2 = adafruit_debouncer.Button(button_2_pin)
buttons.append(button_2)

button_3_pin = digitalio.DigitalInOut(board.A1)
button_3_pin.direction = digitalio.Direction.INPUT
button_3_pin.pull = digitalio.Pull.UP
button_3 = adafruit_debouncer.Button(button_3_pin)
buttons.append(button_3)

main_group.append(background_grid)
main_group.append(tile_grids[current_face])
display.refresh()

current_time = time.monotonic()
last_update = time.monotonic()

# function definitions

# updates current displayed face gif
def change_face(new_face):
    global main_group
    global current_face
        
    main_group.remove(tile_grids[current_face])
    current_face = new_face
    main_group.append(tile_grids[current_face])
    gifs[current_face].next_frame()
    display.refresh()

# advances the background by 1 frame
def update_background():
    global bg_color_start
    global current_background_color

    for y in range(background_bitmap.height):
      current_background_color = y + bg_color_start
      for x in range(background_bitmap.width):
        background_bitmap[x, y] = current_background_color % len(background_colors)
        current_background_color += 1
    bg_color_start += 1

update_background()
change_face(current_face)
current_delay = gifs[current_face].next_frame()

# main loop
while True:
    current_time = time.monotonic()

    # check the state of all defined buttons
    for i in range(len(buttons)):
        buttons[i].update()
        if(buttons[i].pressed):
            change_face(i)
    
    if(current_time - last_update >= current_delay):
        last_update = time.monotonic()

        update_background()
        gifs[current_face].next_frame()
        display.refresh()
