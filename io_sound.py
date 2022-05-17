#!/usr/bin/python

import pygame

class Sound():
	def __init__(self):
        pygame.mixer.init()
        self.sfxCountdown = pygame.mixer.Sound('sound/321activate.wav')
		pass

    def countdown(self):
        self.sfxCountdown.play()
        pass

    def stopCountdown(self):
        self.sfxCountdown.stop()
        pass