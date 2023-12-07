import pygame
from game_parameters import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # self.ouchimage = pygame.transform.scale(pygame.image.load("Assets/runsprites/ouchrun.png"),(125,175)).convert()
        # self.ouchimage.set_colorkey((255, 255, 255))
        self.run_image1 = pygame.transform.scale(pygame.image.load("Assets//playercolor1.png"),(100,150)).convert()
        #anderson helped me with this^^^
        self.run_image1.set_colorkey((255, 255, 255))


        self.image = self.run_image1
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = SCREEN_HEIGHT / 2
        self.speed = 10
        self.size = 1

        self.current_form = 0

        self.run_image2 = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/runimage2test.png"),(100,150)).convert()
        self.run_image2.set_colorkey((255, 255, 255))
        self.run_image3 = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/runimage3test.png"),(100,150)).convert()
        self.run_image3.set_colorkey((255, 255, 255))
        self.run_image4 = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/runimage4.png"),
                                                 (100,150)).convert()
        self.run_image4.set_colorkey((255, 255, 255))
        self.run_image5 = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/runsprites/runimage5.png"),
                                                 (100,150)).convert()
        self.run_image5.set_colorkey((255, 255, 255))

        self.x_velocity = 0  # Initialize x_velocity
        self.y_velocity = 0
    def move_up(self):
        self.y_velocity = -PLAYER_SPEED_UP

    def move_down(self):
        self.y_velocity = PLAYER_SPEED_DOWN

    def move_left(self):
        self.x_velocity = -1 *PLAYER_SPEED
        # self.image = self.reverse_image

    def move_right(self):
        self.x_velocity = PLAYER_SPEED
        # self.image = self.forward_image

    def stop (self):
        self.y_velocity = 0
        self.x_velocity = 0

    def update(self):

        # Update player position based on arrow key input

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

            self.current_form = (self.current_form + 1) % 5

        if self.current_form == 1:
            self.image = self.run_image2


        elif self.current_form == 2:
            self.image = self.run_image3

        elif self.current_form == 3:
            self.image = self.run_image4

        elif self.current_form == 4:
            self.image = self.run_image5

        elif self.current_form == 0:
            self.image = self.run_image2

        # else:
        #     self.image = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/playercolor1.png"),
        #                                         (125, 175)).convert()
        #     self.image.set_colorkey((255, 255, 255))

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

        if self.rect.y < ((SCREEN_HEIGHT//2) -20) - self.rect.height:
            self.rect.y = ((SCREEN_HEIGHT//2) -20) - self.rect.height
        elif self.rect.y > SCREEN_HEIGHT - 170:
            self.rect.y = SCREEN_HEIGHT - 170

    def speed_increase(self, factor):
        self.speed = self.speed*factor
        return self.speed


    def draw(self, screen):
        screen.blit(self.image, self.rect)

PLAYER_SPEED_UP = 10 * PLAYER_SPEED
PLAYER_SPEED_DOWN = 10 * PLAYER_SPEED


