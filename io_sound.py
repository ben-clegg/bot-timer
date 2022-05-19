#!/usr/bin/python

import pygame

class Sound():
    def __init__(self):
        pygame.mixer.init()
        self.sfx321Fight = pygame.mixer.Sound('sound/321Fight.wav')
        self.sfx1MinRemaining = pygame.mixer.Sound('sound/321Fight.wav')
        self.sfx30SecsRemaining = pygame.mixer.Sound('sound/321Fight.wav')
        self.sfxCease = pygame.mixer.Sound('sound/321Fight.wav')
        self.sfxPause = pygame.mixer.Sound('sound/321Fight.wav')
        self.sfxEndingCountdown = pygame.mixer.Sound('sound/Countdown.wav')
        pass

    def countdown(self):
        self.sfx321Fight.play()
        pass
    
    def cease(self):
        self.sfxCease.play()
        pass
    
    def pause(self):
        self.sfxPause.play()
        pass

    def stopAll(self):
        self.sfx321Fight.stop()
        self.sfx1MinRemaining.stop()
        self.sfx30SecsRemaining.stop()
        self.sfxCease.stop()
        self.sfxPause.stop()
        self.sfxEndingCountdown.stop()
        pass