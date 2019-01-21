#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd4in2
import time
from PIL import Image, ImageDraw, ImageFont
import traceback
import Image
import ImageDraw
import time
import os
import random


epd = epd4in2.EPD()
epd.init()
epd.Clear(0xFF)

Himage = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)
draw = ImageDraw.Draw(Himage)
font24 = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 24)
draw.text((10, 0), 'BOBA', font=font24, fill=0)
draw.text((10, 20), '2.9inch e-Paper', font=font24, fill=0)
