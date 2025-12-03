# show a swirly pulsing animation that runs around the outside of a neopixel jewel (7 LEDs)

import time
import board
import neopixel
import random
import adafruit_fancyled.adafruit_fancyled as fancy

color = 0x6E22CD # purple
my_palette = [(0.0, 0x0), 
              (1.0, color)]

palette = fancy.expand_gradient(my_palette, 5)

pixels = neopixel.NeoPixel(board.D2, 7, brightness = 1, auto_write = False, pixel_order = neopixel.GRBW)

# class to store information about each pixel individually
class eachPixel:
  pixel = 0
  palette_index = 0
  curr_color = 0
  increasing = True

p0 = eachPixel()
p1 = eachPixel()
p2 = eachPixel()
p3 = eachPixel()
p4 = eachPixel()
p5 = eachPixel()
p6 = eachPixel()

pixel_list = [p0, p1, p2, p3, p4, p5, p6]

# create a list of random brightnesses to start each pixel with
for i in range(len(pixel_list)):
  this = pixel_list[i]
  this.pixel = pixels[i] # assign pixel to each in list
  this.palette_index = random.uniform(0, 1) # get starting palette index
  this.curr_color = fancy.palette_lookup(palette, this.palette_index) # convert palette index to normalized color
  this.curr_color = fancy.denormalize(this.curr_color) # convert normalized color to RGB
  pixels[i] = this.curr_color

pixels.show()

min = 0.05
max = 1

while True:
  for i in range(len(pixel_list)):
    this = pixel_list[i]
    if this.increasing and this.palette_index < max:
      this.palette_index += 0.01
      this.curr_color = fancy.palette_lookup(palette, this.palette_index)
      this.curr_color = fancy.denormalize(this.curr_color)
      pixels[i] = this.curr_color
    elif not this.increasing and this.palette_index > min:
      this.palette_index -= 0.01
      this.curr_color = fancy.palette_lookup(palette, this.palette_index)
      this.curr_color = fancy.denormalize(this.curr_color)
      pixels[i] = this.curr_color
    else:
      this.increasing = not this.increasing
  
  pixels.show()
  #time.sleep(0.05)