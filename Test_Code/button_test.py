import RPi.GPIO as GPIO
import time

# set integers for the various buttons and LEDs
select_btn = 17
tweet_btn = 27


# set the inputs and outputs from the PiGPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(select_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(tweet_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def debounce():
    time.sleep(0.2)
    
try:
    while True:
        if GPIO.input(select_btn) == False:
            print "The %s has been pressed" % select_btn
            debounce()
        elif GPIO.input(tweet_btn) == False:
            print "The %s has been pressed" % tweet_btn
            debounce()
            
finally:
    GPIO.cleanup()
    

