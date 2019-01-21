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


epd = epd4in2.EPD()
epd.init()
epd.Clear(0xFF)

calendar.setfirstweekday(0) # Monday is the first day of the week

# Calendar strings to be displayed
day_str = time.strftime("%A")
day_number = time.strftime("%d")
month_str = time.strftime("%B") + ' ' + time.strftime("%Y")
month_cal = str(calendar.month(int(time.strftime("%Y")), int(time.strftime("%m"))))
month_cal = month_cal.split("\n",1)[1];
update_moment = time.strftime("%I") + ':' + time.strftime("%M") + ' ' + time.strftime("%p")

w_day_str,h_day_str = font_day_str.getsize(day_str)
x_day_str = (cal_width / 2) - (w_day_str / 2)

# The settings for the Calenday today number in the middle
w_day_num,h_day_num = font_day.getsize(day_number)
x_day_num = (cal_width / 2) - (w_day_num / 2)

# The settings for the month string in the middle
w_month_str,h_month_str = font_month_str.getsize(month_str)
x_month_str = (cal_width / 2) - (w_month_str / 2)

draw_black.rectangle((0,0,240, 384), fill = 0) # Calender area rectangle
draw_black.text((20, 190),month_cal , font = font_cal, fill = 255) # Month calender text
draw_black.text((x_day_str,10),day_str, font = font_day_str, fill = 255) # Day string calender text
draw_black.text((x_day_num,35),day_number, font = font_day, fill = 255) # Day number string text
draw_black.text((x_month_str,150),month_str, font = font_month_str, fill = 255) # Month string text
