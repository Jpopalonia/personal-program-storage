import random

# FNAF 1 door light flicker
light = False

if(random.randint(1, 10) == 1):     # 10% chance for light to flicker off per check
    light = False
else:                               # 90% chance for light to flicker on per check
    light = True