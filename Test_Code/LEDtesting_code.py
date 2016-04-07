import RPi.GPIO as GPIO
import time

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

# this is the testing loop

try:
    while True:
        print "%s on" % t_LED
        GPIO.output(t_LED, True)
        time.sleep(2)
        print "%s off" % t_LED
        time.sleep(2)
        
        print "%s on" % m_LED
        GPIO.output(m_LED, True)
        time.sleep(2)
        print "%s off" % m_LED
        time.sleep(2)
        
        print "%s on" % b_LED
        GPIO.output(b_LED, True)
        time.sleep(2)
        print "%s off" % b_LED
        time.sleep(2)

finally:
    GPIO.cleanup()
        
        