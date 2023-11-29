import pygame
import random

RUNNER_SPEED_MIN = 0.5
RUNNER_SPEED_MAX = 3

class Runner(pygame.sprite.Sprite):


    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("../FinalProject/Assets/runnertest.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.speed = random.uniform(RUNNER_SPEED_MIN, RUNNER_SPEED_MAX)
        self.rect.center = (x, y)
    def update(self, scroll_speed):
        self.rect.x -= scroll_speed


    def draw(self, screen):
        screen.blit(self.image, self.rect)


runners = pygame.sprite.Group()