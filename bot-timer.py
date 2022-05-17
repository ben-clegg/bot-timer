#!/usr/bin/python

import time 
import serial
from io_gui import GUI, UserPermissionException
from io_sound import Sound
from io_button import Button
from state import State
from RPi_WS2812/function_library import *
from RPi_WS2812/neopixel import Adafruit_NeoPixel

# Const
ROUND_TIME_LIMIT = 180 # Time of rounds, in seconds

# Input/Output
gui = GUI()
sound = Sound()
gpio = GPIOAccess()
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.Begin()

# Fields
currentState = State.IDLE
currentTimeSecs = 0.0
paused = False
lastCheckedTime = time.time() 

# State processing
def processState():
	if currentState == State.IDLE:
		idle()
	elif currentState == State.COUNTDOWN:
		countdown()
	elif currentState == State.ACTIVE:
		active()
	elif currentState == State.END:
		end()
	pass

def idle():
	RainbowCycle(strip, .1)
	pass

def countdown():
	if currentTimeSecs < 0:
		currentState = State.ACTIVE
	elif currentTimeSecs <= 1.5:
		FadeInOut(strip, 255, 191, 0)
	else:
		FadeInOut(strip, 255, 0, 0)
	pass

def active():
	if not paused:
		# Green
		RunningLights(strip, 0, 255, 0, .25)
	else:
		# Amber
		RunningLights(strip, 255, 191, 00, .25) 
		
	if currentTimeSecs > ROUND_TIME_LIMIT:
		currentState = State.END
	pass

def end():
	# Red lights
	currentTimeSecs = 0.0
	RunningLights(strip, 255, 0, 0, .25)
	pass

# GUI
def updateGUI():
	timeStr = time.strftime('%M:%S', time.gmtime(round(currentTimeSecs)))
	gui.setTime(timeStr)
	gui.update()
	pass

# Input
def handleShortButton():
	# Idle -> Countdown
	if currentState == State.IDLE:
		currentTimeSecs = 0.0
		paused = False
		currentState = State.COUNTDOWN
	# Countdown -> Idle (abort countdown)
	elif currentState == State.COUNTDOWN:
		sound.stopCountdown()
		currentTimeSecs = 3.0
		currentState = State.IDLE
	# During round - toggle pause
	elif currentState == State.ACTIVE:
		paused = not paused
	# Do nothing for end
	pass

def handleLongButton():
# Reset to idle on long button
	currentState = State.IDLE
	paused = False
	currentTimeSecs = 0.0
	pass

# Time
def stepTime():
	if not paused:
		newTime = time.time()
		if currentState == State.COUNTDOWN:
			currentTimeSecs -= (newTime - lastCheckedTime)
		else:
			currentTimeSecs += (newTime - lastCheckedTime)
		lastCheckedTime = newTime
	else:
		lastCheckedTime = time.time()
	pass


### Main control

# Init button 
button = Button(handleShortButton, handleLongButton)

# Main control loop
while True:
	processState()
	stepTime()
	updateGUI()
