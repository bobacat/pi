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


def choose_random_loading_image(path):
    images = os.listdir(path)
    loading_image = random.randint(0, len(images)-1)
    return path+images[loading_image]


image = Image.open(choose_random_loading_image('bmp/'))

print("read bmp file")
Himage = image
epd.display(epd.getbuffer(Himage))
