import pygame
import math
import sys
from game_parameters import *
from utilities import *
from player import *
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/coinpic.png"),(25, 25)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        self.rect.y = random.randint((SCREEN_HEIGHT / 2) + 50 , SCREEN_HEIGHT - 100 )
        ### ^^^ This controls where the coins generate. I only want them showing up on the bottom half of the screen/ where the road is.

    def update(self, scroll_speed):
        self.rect.x -= scroll_speed

