#!/usr/bin/python

import pygame
import os

class UserPermissionException(Exception):
	pass

S_WIDTH = 800
S_HEIGHT = 480

def centerX(objWidth):
	return (S_WIDTH - objWidth)/2

class GUI:

	def __init__(self):
		#pygame.init()
		self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
		pygame.display.set_caption("BotTimer")
		pygame.font.init()
			
		self.bg    = pygame.image.load(os.path.join("gui", "bg.jpg")).convert()
		#self.title = pygame.image.load(os.path.join("gui", "slugs_logo.png")).convert_alpha()
		
		self.fontTime = pygame.font.SysFont("DejaVu Sans", 48)
		self.fontTime.set_bold(True)

		self.timeText = ""

		self.timeDisplay = self.fontTime.render(self.timeText, 1, (61,61,61))

		pygame.display.toggle_fullscreen()

		self.update()

	def update(self):
		self.screen.fill((0,0,0))
		self.screen.blit(self.bg, (0, 0))
		#self.screen.blit(self.title, (centerX(self.title.get_size()[0]), 40))	
		
		self.screen.blit(self.timeDisplay, (8,424))
		
		pygame.display.flip()

	def setTime(self, timeStr):
		self.timeText = timeStr
	
