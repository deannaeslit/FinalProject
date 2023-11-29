import pygame
from game_parameters import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/playercolor.png"),(125,175)).convert()
        #anderson helped me with this^^^
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = SCREEN_HEIGHT / 2
        self.speed = 5


    def move_up(self):
        self.y_velocity = -PLAYER_SPEED

    def move_down(self):
        self.y_velocity = PLAYER_SPEED

    def move_left(self):
        self.x_velocity = -1 *PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_velocity = PLAYER_SPEED
        self.image = self.forward_image

    def stop (self):
        self.y_velocity = 0
        self.x_velocity = 0

    def update(self):
        keys = pygame.key.get_pressed()

        # Update player position based on arrow key input
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)
