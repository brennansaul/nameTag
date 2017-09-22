# The Dynamic Name Tag 

## Overview:
A do it yourself project that will turn heads at you next job fair. The Dynamic Name Tag uses a Raspberry Pi Zero W and the 2" PaPiRus ink display in order to create a name tag that will change the information displayed every x seconds.

## Materials
- [Raspberry Pi Zero W Budget Pack](https://www.adafruit.com/product/3400)
- [PaPiRus 2 inch ink display](https://www.adafruit.com/product/3335)
- Solder and Wire (Used to attach GPIO pins) or purchase hammer in GPIO pins
- Velcrow stick stick strips
- Portable USB charger

## Assemble 

## Prepare Your Raspberry Pi Zero W
1. Install flash image of either Raspbian Jessie or Jessie Lite to your SD card.
2. Configure your pi: keyboard, locale, time, wifi, enable SPI and I2C interfaces.
3. In the terminal update your Raspberry Pi with the following commands:
    ```
    # Update and Upgrade
    $ apt-get update
    $ apt-get upgrade

    # Restart
    $ sudo shutdown -r now
    ```
4. Install PaPiRus 
    ```
    # When prompted select 2" screen 
    $ curl -sSL https://pisupp.ly/papiruscode | sudo bash
    # After installation your pi will restart
    ```
5. Test that the display is workin properly 
  ```
  $ papirus-test
  ```

## Create youre desired displayes
This is your chance to be creative! Using whatever paint-type program you have in mind create your own name badge. 
Before you start there are some things to keep in mind! The dimentions of the papirus screen is **200x96 pixels**, so before you start creating you display set your canvas to those dimentions. The ink display shows only two colors: white and black. 

Here are the name badge displays that I created on my mac using [PaintBrush](https://paintbrush.sourceforge.io/), a free microsoft paint like software.

#### Base name tag:
In order to have a consistent base display I created this image first and then created duplicates that I added information too. I also used this image so that I styled canvas for displaying system information such as date and time.

![Base name tag picture not found!](https://github.com/brennansaul/nameTag/blob/master/Basenametagbox.png)

#### Education information:
In order to have a consistent base display I created this image first and then created duplicates that I added information too. I also used this image so that I styled canvas for displaying system information such as date and time.

![Base name tag picture not found!](https://github.com/brennansaul/nameTag/blob/master/nametagmajorbox.png)

#### Interests and Hobbies:
In order to have a consistent base display I created this image first and then created duplicates that I added information too. I also used this image so that I styled canvas for displaying system information such as date and time.

![Base name tag picture not found!](https://github.com/brennansaul/nameTag/blob/master/factsnametagbox.png)
 


