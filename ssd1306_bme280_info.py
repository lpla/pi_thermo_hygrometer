# This code is based on
# SPDX-FileCopyrightText: Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from adafruit_bme280 import basic as adafruit_bme280
from adafruit_extended_bus import ExtendedI2C as I2C
import locale

# Set your desired locale for date and time formats
locale.setlocale(locale.LC_ALL, 'ca_ES.utf8@valencia')

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

# Using extended I2C library because I created two I2C buses for my Pi
# First one is for the OLED and second (number 11) is for the temp sensor

# Modify the numbers here to match your setup

# Here take into account that your screen could be 128x32, so change that '64' with '32'
# Also some models like mine have address 0x3C in I2C, but others use 0x3D. Please check it with command like 'i2cdetect' if this value doesn't work.
i2c = I2C(1)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=RESET_PIN)
oled.contrast(1)
# My BME280 model has 0x76 address, but some others have 0x77. Check it with 'i2cdetect' if this value is not working.
i2c11 = I2C(11)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c11, address=0x76)

# This is not even needed as we don't need to calculate altitude, but
# if you need it, just adjust this parameter to your daily sea level pressure
bme280.sea_level_pressure = 1013.25

# Clear display.
oled.poweroff()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

offset = 0  # flips between 0 and 32 for double buffering

while True:
    # write the temperature and humidity from BME280 sensor readings
    draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
    text = "T: %0.1fºC" % bme280.temperature
    draw.text((0, 0), text, font=font2, fill=1)
    text = "H: %0.0f%%" % bme280.relative_humidity
    draw.text((0, 36), text, font=font2, fill=1)
    oled.image(image)
    oled.show()
    oled.poweron()

    # show that for 6 seconds (change if you feel)
    time.sleep(6)

    # poweroff as a transition to avoid burned pixels
    oled.poweroff()
    time.sleep(2)
    oled.poweron()

    # now write the date and time
    draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
    text = time.strftime("%A %e")
    draw.text((0, 0), text, font=font, fill=1)
    text = time.strftime("%b, %Y")
    draw.text((0, 18), text, font=font, fill=1)
    text = time.strftime("%H:%M")
    draw.text((0, 36), text, font=font2, fill=1)
    oled.image(image)
    oled.show()

    # show that for 6 seconds (change if you feel)
    time.sleep(6)

    # another poweroff to keep your screen healthier
    oled.poweroff()
    time.sleep(2)
