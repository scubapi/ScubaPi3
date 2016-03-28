# ScubaPi3
Raspberry Pi in underwater housing with SenseHat and Pi Noir camera


### init.d/pix
This is the script that goes in /etc/init.d.  On the Pi, using 'sudo update-rc.d pix defaults' will set it up to run at boot time.   It starts the pix.sh script which should live in /home/pi

### init.d/hat
This script also goes in /etc/init.d like pix above.    It will start the scrolling marquee with sense data


###  pix.sh
This is the script that actually takes the time lapse photos.   It's set to create a directory, cd to it and then start taking photos every 5 seconds (5000 milliseconds) using raspistill.
Since I used the Pi Noir camera, I set it to night exposure settings

###  scroll.py
Python sense hat code to introduce itself and then get compass, temperature, humdity and acceleration info then scroll it across the screen.


