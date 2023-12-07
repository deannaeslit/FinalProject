import pygame
import random
from game_parameters import *
import math
import player


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/enemytest.png"), (100, 100)).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT -150)
        self.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
        self.rect.center = (x, y)

    def update(self, scroll_speed, player):
        self.rect.x -= (self.speed - scroll_speed)


        ## reset more enemies

        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH + random.randint(50, 200)
            self.rect.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT -150)
            self.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)

        # dx = player.rect.x - self.rect.x
        # dy = player.rect.y - self.rect.y
        # distance = math.sqrt(dx ** 2 + dy ** 2)
        #
        # # Normalize the direction vector
        # if distance != 0:
        #     dx /= distance
        #     dy /= distance
        #
        # if player.rect.x < self.rect.x:
        #     # Update the enemy's position based on the normalized direction vector and speed
        #     self.rect.x += dx * self.speed - scroll_speed
        #     self.rect.y += dy * self.speed

            # Remove the enemy if it goes off the left side of the screen
        if self.rect.right < 0:
            self.kill()


            # Reset the enemy if it goes off the screen
        if self.rect.right < 0:
            self.reset_position()

    def reset_position(self):
        self.rect.x = SCREEN_WIDTH + random.randint(50, 200)
        self.rect.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - 150)
        self.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

enemies = pygame.sprite.Group()