import RPi.GPIO as GPIO
import time

# set integers for the various buttons and LEDs
select_btn = 17
tweet_btn = 27


# set the inputs and outputs from the PiGPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(select_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(tweet_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# this is the button debounce function
def debounce():
    time.sleep(0.4)
    
# set the choice fucntion to 0 [it can ahve values 0,1,2]
tweet_choice = 0

try:
    while True:
        if GPIO.input(select_btn) == False:
            print "The %s has been pressed" % select_btn
            if tweet_choice == 0:
                tweet_choice = 1
                print "New tweet choice: %s" % tweet_choice
            elif tweet_choice == 1:
                tweet_choice = 2
                print "New tweet choice: %s" % tweet_choice
            else:
                tweet_choice = 0
                print "New tweet choice: %s" % tweet_choice
            debounce()
        elif GPIO.input(tweet_btn) == False:
            print "The %s has been pressed" % tweet_btn
            debounce()
            
finally:
    GPIO.cleanup()
