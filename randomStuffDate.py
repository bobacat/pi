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


def main():
    epd = epd4in2.EPD()
    epd.init()
    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.open(choose_random_loading_image('images/'))
    now = datetime.datetime.now()
    currentDate = (now.strftime("%Y-%m-%d"))
    localtime = (now.strftime("%H:%M:%S"))
    draw = ImageDraw.Draw(Himage)
    font24 = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 24)
    draw.text((10, 0), 'Text', font = font24, fill = 0)
    draw.text((0, 100), currentDate, font = font24, fill = 0)
    draw.text((0, 200), localtime, font = font24, fill = 0)
    epd.display(epd.getbuffer(Himage))
    epd.display(epd.get_frame_buffer(image))
    time.sleep(10)  # change the image every minute
    main()


if __name__ == '__main__':
    main()
