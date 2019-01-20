#!/usr/local/bin/python
# -*- coding: utf-8 -*-
##

import epd4in2
import Image
import ImageDraw
import ImageFont
import calendar
import time
import requests
import sys
import urllib
import json
import urllib2
import operator
import os
import random
import threading

reload(sys)
sys.setdefaultencoding('utf-8')
# import imagedata

EPD_WIDTH = 400
EPD_HEIGHT = 300

TODOIST_TOKEN = 'fb4025841776e8e14315bf4e21da0fe99ac35ecd'
todolist_items = 0


def main():

        displayTasks()
        wait = 60
        refresh_time = 1000
        start_time = time.time()+refresh_time

        while True:
            print('restart  : current time ' + str(time.time()/60) + ' started time ' + str(start_time/60))
            if is_todo_changed():
                start_time=time.time()+refresh_time  # rest refresh time
                displayTasks()
            elif (time.time()-start_time)>0:
                start_time=time.time()+refresh_time  # rest refresh time
                displayTasks()

            time.sleep(wait)


def is_todo_changed():
    response = requests.get("https://beta.todoist.com/API/v8/tasks", params={"token":TODOIST_TOKEN}).json()
    global todolist_items
    get_todolist_items= len (response)

    if(get_todolist_items!=todolist_items):
        print('items chnaged')
        return True


def restart_program():
    displayTasks()


def choose_random_loading_image():
    images = os.listdir("bmp/")
    loading_image = random.randint(0, len(images)-1)
    return images[loading_image]


def displayTasks():
    epd = epd4in2.EPD()
    epd.init()

    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    image = Image.open('bmp/'+choose_random_loading_image())
    epd.display_frame(epd.get_frame_buffer(image))

    response = requests.get("https://beta.todoist.com/API/v8/tasks", params={"token":TODOIST_TOKEN}).json()
    data = response
    global todolist_items
    todolist_items = len(data)

    calendar.setfirstweekday(6)  # set the first day of the week
    LINEHEIGHT = 20

    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 20)
    font_cal = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
    font_day = ImageFont.truetype('fonts/Roboto-Black.ttf', 110)
    font_day_str = ImageFont.truetype('fonts/Roboto-Light.ttf', 35)
    font_month_str = ImageFont.truetype('fonts/Roboto-Light.ttf', 25)

    font_weather_icons = ImageFont.truetype('fonts/weathericons-regular-webfont.ttf', 35)
    font_weather_degree = ImageFont.truetype('fonts/Roboto-Light.ttf', 25)
    font_tasks_list_title = ImageFont.truetype('fonts/Roboto-Light.ttf',30)
    font_tasks_list = ImageFont.truetype('fonts/tahoma.ttf',12)
    font_tasks_due_date = ImageFont.truetype('fonts/tahoma.ttf',9)
    salahFont = ImageFont.truetype('fonts/arial.ttf', 13)
    salahFont2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 14)

    font_icons = ImageFont.truetype('fonts/Byom-Icons-Trial.ttf', 15)

# Calendar Strings
    cal_day_str = time.strftime("%A")
    cal_day_number = time.strftime("%d")
    cal_month_str = time.strftime("%B")+' '+time.strftime("%Y")

    cal_month_cal = str(calendar.month(2017, 10)).replace(time.strftime("%B")+' ' + time.strftime("%Y"), ' ')

    cal_width=240

    # this section is to center the calendar text in the middle

    # the Day string "Monday" for Example
    w_day_str, h_day_str = font_day_str.getsize(cal_day_str)
    x_day_str = (cal_width/2)-(w_day_str/2)
    # y_day_str=(epd2in9.EPD_HEIGHT/2)-(h/2)

    # the settings for the Calenday today number
    w_day_num, h_day_num = font_day.getsize(cal_day_number)
    x_day_num = (cal_width/2)-(w_day_num/2)

    # the settings for the Calenday Month String
    w_month_str, h_month_str = font_month_str.getsize(cal_month_str)
    x_month_str = (cal_width/2)-(w_month_str/2)

    # the settings for the Calenday display (didn't work)
    # w_month_cal_str,h_month_cal_str=font_day_str.getsize(cal_month_cal)
    # x_month_cal_str=(cal_width/2)-(w_month_cal_str/2)

    draw.rectangle((0, 0, 240, 384), fill=0)
    draw.text((15, 190), cal_month_cal, font=font_cal, fill=255)
    draw.text((x_day_str, 25), cal_day_str, font=font_day_str, fill=255)
    draw.text((x_day_num, 50), cal_day_number, font=font_day, fill=255)
    draw.text((x_month_str, 165), cal_month_str, font=font_month_str, fill=255)

    draw.rectangle((245, 5, 635, 55), fill=0)
    draw.text((250, 10), "Tasks ", font=font_tasks_list_title, fill=255)
    # draw.text((620,30),"K",font=font_icons,fill=255)  #lock icon
    for task in data:
        item = str(task['content'])
        priority = str(task['priority'])
        if(len(item) > 55):
            item = item[0:55]+'...'
        draw.text((265, 60+LINEHEIGHT), item, font=font_tasks_list, fill=0)

        if int(priority) > 2:
            # draw.rectangle((245,65+LINEHEIGHT, 255, 75+LINEHEIGHT), fill = 0)
            draw.chord((246, 62+LINEHEIGHT, 256, 72+LINEHEIGHT), 0, 360, fill=0)
            draw.text((250, 62+LINEHEIGHT), priority, font=font_tasks_due_date, fill=255)

        if 'due' in task:
            draw.rectangle((595,68+LINEHEIGHT, 630, 78+LINEHEIGHT), fill = 0)
            draw.text((600,68.5+LINEHEIGHT),str(task['due']['string']),font=font_tasks_due_date,fill=255)

        # draw.rectangle((250,67.5+LINEHEIGHT, 255, 72.5+LINEHEIGHT), fill = 0)
        # draw.rectangle((251,66+LINEHEIGHT, 254, 70+LINEHEIGHT), fill = 255)
        # draw.chord((250,68+LINEHEIGHT, 255, 73+LINEHEIGHT), 0, 360, fill = 0)
        draw.arc((247.5,62+LINEHEIGHT, 257.5, 72+LINEHEIGHT), 0, 360, fill=0)
        draw.line((250, 78+LINEHEIGHT, 630, 78+LINEHEIGHT), fill=0)
        LINEHEIGHT = 26
        print(task['content'])

    # draw.text((250,100),data[2]["content"],font=font_tasks_list,fill=0)

    epd.display_frame(epd.get_frame_buffer(image))

    # You can get frame buffer from an image or import the buffer directly:
    # epd.display_frame(imagedata.MONOCOLOR_BITMAP)


if __name__ == '__main__':
    main()
