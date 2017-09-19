#!/usr/bin/python

import time
import sys 
import os


from datetime import datetime

import Image
import ImageDraw
import ImageFont

from papirus import Papirus
from papirus import PapirusImage
from papirus import PapirusTextPos

import datetime

# Set Screen rotation
# Optional rotation argument: rot = 0, 90, 180 or 270
#screen = Papirus(0)
image = PapirusImage(180)
text = PapirusTextPos(180)

#Display loop
while True:
  # 1 Original Screen Major / Minor / Graduation displays for 15 seconds
  # Write a bitmap to the epaper screen
  image.write('./nametagmajorbox.png')

  # Update only the changed pixels (faster)
  #screen.update()

  # wait for 15 seconds
  time.sleep(10)

  # 2 Display Hobbies and Interests 10 seconds

  # Write a bitmap to the epaper screen
  image.write('./factsnametagbox.png')

  # Update only the changed pixels (faster)
  #screen.partial_update()

  # wait for 15 seconds
  time.sleep(10)

  # Time Display 
  t = datetime.datetime.now()
  timeString = t.strftime("%H:%M")
  image.write('./Basenametagbox.png')
  text.AddText(timeString, 150, 80, Id="Start")
  
  time.sleep(10)
  text.Clear()
