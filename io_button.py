#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class Button:

    PIN_BUTTON = 12
    LONG_PRESS_THRESHOLD = 1.0

    def __init__(self, functionShortPress, functionLongPress):
        GPIO.setmode(GPIO.BOARD)
        # Initialise GPIO inputs in pull-up resistor mode
        GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        self.shortPressFunc = functionShortPress
        self.longPressFunc = functionLongPress
        self.pressStartTime = 0.0
        
        GPIO.add_event_detect(buttonPin, GPIO.RISING, callback = pressStarted, bouncetime=300)
        GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = pressEnded, bouncetime=300)
    
        pass

    def pressStarted(self, channel):
        self.pressStartTime = time.time()
        pass

    def pressEnded(self, channel):
        pressLength = time.time() - self.pressStartTime

        if (pressLength < LONG_PRESS_THRESHOLD):
            self.shortPressFunc()
        else:
            self.longPressFunc()

        pass
    
    def update(self):
        pass