# !/usr/bin/python
# -*- coding:utf-8 -*-
# !/usr/bin/python
import spidev as SPI  # where the display connects
import Image
import ImageDraw
import ImageFont  # PIL - PythonImageLibrary
import time
import datetime
import sys
import signal
import urllib
import requests
import random
from StringIO import StringIO
from EPD_driver import EPD_driver
import epd4in2
import traceback

try:
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear(0xFF)

    # Drawing on the Horizontal image
    # 255: clear the frame
    Himage = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)
    # Drawing on the Vertical image
    Limage = Image.new('1', (epd4in2.EPD_HEIGHT, epd4in2.EPD_WIDTH), 255)

    # Horizontal
    print("Drawing")
    now = datetime.datetime.now()
    currentDate = (now.strftime("%Y-%m-%d"))
    localtime = (now.strftime("%H:%M:%S"))
    draw = ImageDraw.Draw(Himage)
    font24 = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 24)
    draw.text((10, 0), 'BOBA IS A BIG WEINER!!', font=font24, fill=0)
    draw.text((0, 100), currentDate, font=font24, fill=0)
    draw.text((0, 200), localtime, font=font24, fill=0)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    epd.sleep()


# mainimg is used as screen buffer, all image composing/drawing is done in PI$
# the mainimg is then copied to the display (drawing on the disp itself is no$

except:
    print('traceback.format_exc():\n%s' % traceback.format_exc())
    exit()
