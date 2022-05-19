#!/usr/bin/python

import RPi.GPIO as GPIO
import time

PIN_BUTTON = 12
LONG_PRESS_THRESHOLD = 1.0
    
class Button:

    def __init__(self, functionShortPress, functionLongPress):
        GPIO.setmode(GPIO.BOARD)
        # Initialise GPIO inputs in pull-up resistor mode
        GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        self.shortPressFunc = functionShortPress
        self.longPressFunc = functionLongPress
        self.pressStartTime = 0.0
        
        GPIO.add_event_detect(PIN_BUTTON, GPIO.BOTH, callback = self.pressChange, bouncetime=300)
    
        pass
    
    def pressChange(self, channel):
        # Check high or low, determine if rose / fell
        if GPIO.input(PIN_BUTTON):
            self.pressStarted()
        else:
            self.pressEnded()
        pass

    def pressStarted(self):
        self.pressStartTime = time.time()
        pass

    def pressEnded(self):
        pressLength = time.time() - self.pressStartTime

        if (pressLength < LONG_PRESS_THRESHOLD):
            self.shortPressFunc()
        else:
            self.longPressFunc()

        pass
    
    def update(self):
        pass