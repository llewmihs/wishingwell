# import the necessary modules: the GPIO, Twython, Time and the PiCamera

import RPi.GPIO as GPI
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


# open and load the config file for the Twitter client (Twython)
config = {}
execfile("wishing_tweet_conf.py", config)

# create the Twitter API object
twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])

# the three Tweets (to rule them all)
tweet1 = "This is the first Tweet"
tweet2 = "This is the second Tweet"
tweet3 = "This is the third Tweet"

# initialise the tweet choice to 1
current_tweet = 1

# code to run
try:
  while True:
      select_btn_state = GPIO.input(select_btn)
      tweet_btn_state = GPIO.input(tweet_btn)
      if select_btn_state == False:
        print "Changing tweet selection"
        if current_tweet == 1:
          current_tweet == 2
          GPIO.ouput(t_LED, False)
          GPIO.output(m_LED, True)
          GPIO.output(b_LED, False)
          time.sleep(0.2)
          
        elif current_tweet == 2:
          current_tweet == 3
          GPIO.ouput(t_LED, False)
          GPIO.output(m_LED, True)
          GPIO.output(b_LED, False)
          time.sleep(0.2)
          
        else:
          current_tweet == 1
          GPIO.ouput(t_LED, True)
          GPIO.output(m_LED, False)
          GPIO.output(b_LED, False)
          time.sleep(0.2)
        

finally:
  GPIO.cleanup()



