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
import calendar
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

    # Drawing on the Horizontal image
    # 255: clear the frame




    Himage = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)
    # Drawing on the Vertical image
    Limage = Image.new('1', (epd4in2.EPD_HEIGHT, epd4in2.EPD_WIDTH), 255)



    font_cal = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 12)
    font_day = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 60)
    font_weather = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 20)
    font_day_str = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 12)
    font_month_str = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 12)
    font_weather_icons = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 40)
    font_tasks_list_title = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 10)
    font_tasks_list = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 12)
    font_tasks_due_date = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 11)
    font_tasks_priority = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 9)
    font_update_moment = ImageFont.truetype('amiga_forever/amiga4ever.ttf', 9)

    # Horizontal
    print("Drawing")
    now = datetime.datetime.now()
    currentDate = (now.strftime("%Y-%m-%d"))
    localtime = (now.strftime("%H:%M:%S"))
    draw = ImageDraw.Draw(Himage)

    calendar.setfirstweekday(0)  # Monday is the first day of the week

    # Calendar strings to be displayed

    cal_width = 100
    line_start = 20
    day_str = time.strftime("%A")
    day_number = time.strftime("%d")
    month_str = time.strftime("%B")  # + ' ' + time.strftime("%Y")
    month_cal = str(calendar.month(int(time.strftime("%Y")), int(time.strftime("%m"))))
    month_cal = month_cal.split("\n", 1)[1]
    update_moment = time.strftime("%I") + ':' + time.strftime("%M") + ' ' + time.strftime("%p")

    # This section is to center the calendar text in the middle
    w_day_str,h_day_str = font_day_str.getsize(day_str)
    x_day_str = 400 - (cal_width / 2) - (w_day_str / 2)

    # The settings for the Calenday today number in the middle
    w_day_num,h_day_num = font_day.getsize(day_number)
    x_day_num = 400 - (cal_width / 2) - (w_day_num / 2)

    # The settings for the month string in the middle
    w_month_str,h_month_str = font_month_str.getsize(month_str)
    x_month_str = 400 - (cal_width / 2) - (w_month_str / 2)

    image_black = Image.open('4in2.bmp')
    image_draw = Image.open('image_black')
    image_draw.rectangle((0, 175, 400, 300), fill=0)  # Calender area rectangle
    image_draw.text((20, 190),month_cal , font=font_cal, fill = 255)  # Month calender text
    image_draw.text((x_day_str, 190),day_str, font=font_day_str, fill = 255)  # Day string calender text
    image_draw.text((x_day_num, 210),day_number, font=font_day, fill = 255)  # Day number string text
    image_draw.text((x_month_str, 270),month_str, font=font_month_str, fill = 255)  # Month string text
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    epd.sleep()


# mainimg is used as screen buffer, all image composing/drawing is done in PI$
# the mainimg is then copied to the display (drawing on the disp itself is no$

except:
    print('traceback.format_exc():\n%s' % traceback.format_exc())
    exit()
