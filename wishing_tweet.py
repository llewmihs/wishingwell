# import the necessary modules: the GPIO, Twython, Time and the PiCamera

import RPi.GPIO as GPI
import time
from twython import Twython
import picamera

# set the inputs and outputs from the PiGPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


# open and load the config file for the Twitter client (Twython)
config = {}
execfile("wishing_tweet_conf.py", config)

# create the Twitter API object
twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])

