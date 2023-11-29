import pygame
import sys
import random
from game_parameters import *
from enemy import Enemy

enemies = pygame.sprite.Group()

def draw_background(surf):
    # Load tiles from the assets folder into surfaces
    road = (pygame.transform.scale(pygame.image.load("../FinalProject/assets/game_background.png"),
                                   (800, 600)).convert())
    # use the png transparency
    road.set_colorkey((0, 0, 0))

    surf.blit(road, (0, 0))

    # draw the title at the top center of the screen
    custom_font = pygame.font.Font("../FinalProject/assets/fonts/Black_Crayon.ttf", 48)
    text = custom_font.render("Hopper Run!", True, (255, 69, 0))
    surf.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))


def add_runner(num_runners):
    for _ in range(num_runners):
        runners.add(Runner(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), random.randint(TILE_SIZE, SCREEN_HEIGHT
                                                                                          - TILE_SIZE)))
def add_enemies(num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2),
        random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))