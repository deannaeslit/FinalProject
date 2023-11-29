import pygame
import math
import sys
from game_parameters import *
from utilities import *
from player import *
import random
from runner import *
from coins import Coin
from enemy import Enemy




clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using tiles and blit to draw tiles")


##life icons
life_icon = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/runnertest.png"),(50,50)).convert()
life_icon.set_colorkey((0, 0, 0))

clock = pygame.time.Clock()

road = (pygame.transform.scale(pygame.image.load("../FinalProject/assets/game_background.png"), (800, 600)).convert())

scroll = 0
enemies = pygame.sprite.Group()

tiles = math.ceil(SCREEN_WIDTH / road.get_width()) + 1

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
add_enemies(3)

coins = pygame.sprite.Group()


## make coins pop up

for _ in range(2):
    coin = Coin()
    coin.image.set_colorkey((255, 255, 255))
    coins.add(coin)



score = 0
lives = NUM_LIVES
score_font = pygame.font.Font("../FinalProject/assets/fonts/Black_Crayon.ttf", 48)




###MAIN LOOP####


while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.stop()

    clock.tick(33)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Continuous scrolling to the left
    scroll -= 6

    screen.fill((255, 255, 255))
## road time!!!!

    for i in range(-1, tiles + 1):
        screen.blit(road, (road.get_width() * i + scroll, 0))

    custom_font = pygame.font.Font("../FinalProject/assets/fonts/Black_Crayon.ttf", 48)
    text = custom_font.render("Hopper Run!", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

##reset scroll
    if abs(scroll) > road.get_width():
        scroll = 0

    # Generate coins randomly at a slower rate
    if random.randint(0, 100) < 2:
        coin = Coin()
        coin.image.set_colorkey((255, 255, 255))
        coins.add(coin)


### UPDATING AND DRAWING##
    coins.update(scroll_speed=6)
    coins.draw(screen)
    enemies.update(scroll_speed = 6)
    enemies.draw(screen)

    ### trying to animate the sprites

#some changes

    player.update()
    screen.blit(player.image, player.rect)
    player.image.set_colorkey((0, 0, 0))


## check for collisions between player and coins
    result = pygame.sprite.spritecollide(player, coins, True)
    if result:
        score += len(result)

    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        lives -= len(result)
    # add new fish
        add_enemies(len(result))

    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
    add_enemies(1)

    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    pygame.display.update()




