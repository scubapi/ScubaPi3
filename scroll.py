#!/usr/bin/python
import sys
from sense_hat import SenseHat
import time

# To get good results with the magnetometer you must first calibrate it using
# the program in RTIMULib/Linux/RTIMULibCal
# The calibration program will produce the file RTIMULib.ini
# Copy it into the same folder as your Python code

led_loop = [4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 57, 56, 48, 40, 32, 24, 16, 8, 0, 1, 2, 3]

sense = SenseHat()
sense.set_rotation(0)
sense.clear()

prev_x = 0
prev_y = 0

led_degree_ratio = len(led_loop) / 360.0

sense.set_rotation(0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

while True:
    sense.show_message("Hi!  I'm ScubaPi", text_colour=red)
    dir = sense.get_compass()
    mytemp = sense.get_temperature()
    myhumid = sense.get_humidity()
    myacc = sense.get_accelerometer()
#    print "Direction  " + str(round(dir,1)) + " Temp " +str(round(mytemp,1)) + " Humidity " + str(round(myhumid,1))
#    print "Pitch " + str(round(myacc['pitch'],1)) + " Yaw " + str(round(myacc['yaw'],1)) + " Roll " + str(round(myacc['roll'],1))
    sense.show_message( "Direction  " + str(round(dir,1)) + " Temp " +str(round(mytemp,1)) + " Humidity " + str(round(myhumid,1)), text_colour=green)
    sense.show_message("Pitch " + str(round(myacc['pitch'],1)) + " Yaw " + str(round(myacc['yaw'],1)) + " Roll " + str(round(myacc['roll'],1)), text_colour=blue)
#    dir_inverted = 360 - dir  # So LED appears to follow North
#    led_index = int(led_degree_ratio * dir_inverted)
#    offset = led_loop[led_index]

#    y = offset // 8  # row
#    x = offset % 8  # column

#    if x != prev_x or y != prev_y:
#        sense.set_pixel(prev_x, prev_y, 0, 0, 0)

#    sense.set_pixel(x, y, 0, 0, 255)

#    prev_x = x
#    prev_y = y

    time.sleep(1)
