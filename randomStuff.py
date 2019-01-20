#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd4in2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear(0xFF)

    def choose_random_loading_image(path):
        images = os.listdir(path)
        loading_image = random.randint(0,len(images)-1)
        return path+images[loading_image]

        def main():
            epd = epd4in2.EPD()
            epd.init()
            # For simplicity, the arguments are explicit numerical coordinates
            image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
            draw = ImageDraw.Draw(image)
            image = Image.open(choose_random_loading_image('bmp/'))
            epd.display_frame(epd.get_frame_buffer(image))
            time.sleep(60)  # change the image every minute
            main()

            if __name__ == '__main__':
                main()

    # Drawing on the Horizontal image
    Himage = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)  # 255: clear the frame
    # Drawing on the Vertical image
    Limage = Image.new('1', (epd4in2.EPD_HEIGHT, epd4in2.EPD_WIDTH), 255)  # 255: clear the frame

    # Horizontal
    print "Drawing"
    draw = ImageDraw.Draw(Himage)
    font24 = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 24)
    draw.text((10, 0), 'BOBA IS A BIG WEINER!!', font = font24, fill = 0)
    draw.text((10, 20), '2.9inch e-Paper', font = font24, fill = 0)
    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    # Vertical
    draw = ImageDraw.Draw(Limage)
    font18 = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 18)
    draw.text((2, 0), 'BOBA IS A BIG FAT LOSER! BUT HES SOFT AND I LOVE HIM!', font = font18, fill = 0)
    draw.text((2, 20), '2.9inch epd', font = font18, fill = 0)
    draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
    draw.line((10, 90, 60, 140), fill = 0)
    draw.line((60, 90, 10, 140), fill = 0)
    draw.rectangle((10, 90, 60, 140), outline = 0)
    draw.line((95, 90, 95, 140), fill = 0)
    draw.line((70, 115, 120, 115), fill = 0)
    draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw.rectangle((10, 150, 60, 200), fill = 0)
    draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Limage))
    time.sleep(2)

    print "read bmp file"
    Himage = Image.open('4in2.bmp')
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    print "read bmp file on window"
    Himage2 = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)  # 255: clear the frame
    bmp = Image.open('100x100.bmp')
    Himage2.paste(bmp, (50,10))
    epd.display(epd.getbuffer(Himage2))
    time.sleep(2)

    epd.sleep()

except:
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    exit()
