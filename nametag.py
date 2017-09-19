#!/usr/bin/python

from papirus import Papirus
import time

# Set Screen rotation
# Optional rotation argument: rot = 0, 90, 180 or 270
screen = Papirus([rotation = 0])


#Display loop
#while True:
  # 1 Original Screen Major / Minor / Graduation displays for 15 seconds
  # Write a bitmap to the epaper screen
  screen.display('./nametagmajorbox.png')

  # Update only the changed pixels (faster)
  screen.update()

  # wait for 15 seconds
  time.sleep(10)

  # 2 Display Hobbies and Interests 10 seconds

  # Write a bitmap to the epaper screen
  screen.display('./factsnametagbox.png')

  # Update only the changed pixels (faster)
  screen.partial_update()

  # wait for 15 seconds
  time.sleep(1)

  # Time Display 
