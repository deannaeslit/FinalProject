import pygame
import random
from game_parameters import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/Enemyimage.png"), (50, 50)).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 50
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 30)
        self.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
        self.rect.center = (x, y)

    def update(self, scroll_speed):
        self.rect.x -= scroll_speed


    def draw(self, screen):
        screen.blit(self.image, self.rect)
