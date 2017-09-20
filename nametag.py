#!/usr/bin/python

import time
import sys 
import os

import Image
import ImageDraw
import ImageFont

from papirus import Papirus
from papirus import PapirusImage
from papirus import PapirusComposite

import datetime

# Set Screen rotation
# Optional rotation argument: rot = 0, 90, 180 or 270
image = PapirusImage(180)


#Display loop
while True:
  # 1 Original Screen Major / Minor / Graduation displays for 15 seconds
  # Write image to the epaper screen
  image.write('./nametagmajorbox.png')

  # Wait / display for 15 seconds
  time.sleep(15)
  #time.sleep(3) # For dev

  # 2 Display Hobbies and Interests 15 seconds
  # Write image to the epaper screen
  image.write('./factsnametagbox.png')

  # Wait / display for 10 seconds
  time.sleep(10)
  #time.sleep(3) # For Dev
  
  # 3 Display Time and Date 10 seconds 
  # Calling PapirusComposite this way will mean nothing is written to the screen until WriteAll is called
  textNImg = PapirusComposite(False, 180)
  
  # String storing time and data into respective strings
  t = datetime.datetime.now()
  timeString = t.strftime("%I:%M %p")
  dateString = t.strftime("%a %b %d")

  # Add image with default layout date text and time text
  textNImg.AddImg("./Basenametagbox.png", 0, 0, (200, 96), Id="NameLogo")
  textNImg.AddText(dateString, 65, 20, Id="date")
  textNImg.AddText(timeString, 65, 40, Id="time")

  # Now display all elements on the scrren
  textNImg.WriteAll()
  
  time.sleep(10)
  #time.sleep(3) For Dev
