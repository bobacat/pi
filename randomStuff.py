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

try:
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear(0xFF)

    Himage = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)
    # Drawing on the Vertical image
    Limage = Image.new('1', (epd4in2.EPD_HEIGHT, epd4in2.EPD_WIDTH), 255)

    def choose_random_loading_image(path):
        images = os.listdir(path)
        loading_image = random.randint(0, len(images)-1)
        return path+images[loading_image]

    def main():
        epd = epd4in2.EPD()
        epd.init()
        # For simplicity, the arguments are explicit numerical coordinates
        image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)
        draw = ImageDraw.Draw(Himage)
        image = Image.open(choose_random_loading_image('bmp/'))
        epd.display_frame(epd.get_frame_buffer(image))
        time.sleep(60)  # change the image every minute
        main()

        if __name__ == '__main__':
            main()

    except:
        print 'traceback.format_exc():\n%s' % traceback.format_exc()
        exit()
