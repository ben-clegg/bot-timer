#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class Button:

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)

		# GPIO Pin definitions
		
		self.p_led = [13,19]
		self.p_led[0] = 13 # Green
		self.p_led[1] = 19 # Red
		self.p_buzzer = 22		
		GPIO.setup(self.p_led[0], GPIO.OUT)
		GPIO.setup(self.p_led[1], GPIO.OUT)
		GPIO.setup(self.p_buzzer, GPIO.OUT)
		
		# Set all on
		GPIO.output(self.p_led[0], True)	
		GPIO.output(self.p_led[1], True)	
		GPIO.output(self.p_buzzer, True)	
		
		time.sleep(1)

		# Set all off
		GPIO.output(self.p_led[0], False)	
		GPIO.output(self.p_led[1], False)	
		GPIO.output(self.p_buzzer, False)	

		pass
	
	def update(self):
		pass