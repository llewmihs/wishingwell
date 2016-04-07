import RPi.GPIO as GPIO
import time
from twython import Twython
import picamera

# set integers for the various buttons and LEDs
select_btn = 17
tweet_btn = 27
t_LED = 22
m_LED = 23
b_LED = 24


# set the inputs and outputs from the PiGPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(select_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(tweet_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(t_LED, GPIO.OUT)
GPIO.setup(m_LED, GPIO.OUT)
GPIO.setup(b_LED, GPIO.OUT)

# initialise the LEDs as off to begin with
GPIO.output(t_LED, False)
GPIO.output(m_LED, False)
GPIO.output(b_LED, False)

# this is the button debounce function
def debounce():
    time.sleep(0.4)
    
def light_switch(top, middle, bottom):
    GPIO.output(t_LED, top)
    GPIO.output(m_LED, middle)
    GPIO.output(b_LED, bottom)
    
# set the choice fucntion to 0 [it can ahve values 0,1,2]
tweet_choice = 0
light_switch(True, False, False)

try:
    while True:
        if GPIO.input(select_btn) == False:
            print "The %s has been pressed" % select_btn
            if tweet_choice == 0:
                tweet_choice = 1
                light_switch(True, False, False)
                print "New tweet choice: %s" % tweet_choice
            elif tweet_choice == 1:
                tweet_choice = 2
                light_switch(False, True, False)
                print "New tweet choice: %s" % tweet_choice
            else:
                tweet_choice = 0
                light_switch(False, False, True)
                print "New tweet choice: %s" % tweet_choice
            debounce()
        elif GPIO.input(tweet_btn) == False:
            print "The %s has been pressed" % tweet_btn
            debounce()
            
finally:
    GPIO.cleanup()
