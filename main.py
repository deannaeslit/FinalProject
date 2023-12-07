import pygame
import math
import sys
from game_parameters import *
from utilities import *
from player import *
import random
from coins import Coin
from enemy import Enemy
import pygame.mixer
from apple import Apple
import time


pygame.init()
pygame.mixer.init()
menumusic = pygame.mixer.music.load("../FinalProject/Assets/sounds/MainMenu.mp3")


pygame.mixer.music.stop()


pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


clock = pygame.time.Clock() 


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
mainmenu(screen, menumusic)
pygame.display.set_caption("Using tiles and blit to draw tiles")

ouch = pygame.mixer.Sound("../FinalProject/Assets/sounds/oof.mp3")
ouchimage = pygame.transform.scale(pygame.image.load("Assets/runsprites/ouchrun.png"),(200,300)).convert()
ouchimage.set_colorkey((255, 255, 255))

##life icons
life_icon = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/playercolorwhite.png"),(50,50)).convert()
life_icon.set_colorkey((0, 0, 0))

## cutscene

cutscene(screen)

susmusic = pygame.mixer.music.load("../FinalProject/Assets/sounds/dundundun.mp3")
cutscene2(screen, susmusic)

clock = pygame.time.Clock()

road = (pygame.transform.scale(pygame.image.load("../FinalProject/assets/backgroundtest.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)).convert())

scroll = 0


tiles = math.ceil(SCREEN_WIDTH / road.get_width()) + 1

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)



coins = pygame.sprite.Group()
apples = pygame.sprite.Group()

apple_effect_start_time = 0
apple_effect_duration = 3000

## make coins pop up

for _ in range(2):
    coin = Coin()
    coin.image.set_colorkey((255, 255, 255))
    coins.add(coin)



score = 0
lives = NUM_LIVES
score_font = pygame.font.Font("../FinalProject/assets/fonts/Black_Crayon.ttf", 48)


add_enemies(2)

###MAIN LOOP####
pygame.mixer.music.stop()
pygame.mixer.music.load("../FinalProject/Assets/sounds/gamemusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

starttime = pygame.time.get_ticks()
ENEMY_SPEED_INCREASE_RATE = 2
ENEMY_SPAWN_INTERVAL = 2000
currenttime = pygame.time.get_ticks()
timepass = (currenttime - starttime) / 1000

while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.stop()

    clock.tick(30)


    #Continuous scrolling to the left
    scroll -= 8.5




## road time!!!!

    for i in range(-1, tiles + 1):
        screen.blit(road, (road.get_width() * i + scroll, 0))



        if random.randint(0, 100000000) < 30:
            enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT -175)
            enemy.image.set_colorkey((255, 255, 255))
            enemies.add(enemy)


##reset scroll
    if abs(scroll) > road.get_width():
        scroll = 0

    # Generate coins randomly at a slower rate
    if random.randint(0, 100) < 2:
        coin = Coin()
        coin.image.set_colorkey((255, 255, 255))
        coins.add(coin)

    if random.randint(0, 100) < .5:
        apple = Apple()
        # apple.image.set_colorkey((255, 255, 255))
        apples.add(apple)

    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)

    ### UPDATING AND DRAWING##

    #enemies.draw(screen)
    coins.update(scroll_speed=9)
    apples.update(scroll_speed=9)
    for enemy in enemies:
        enemy.update(scroll_speed=-7 - timepass * (ENEMY_SPEED_INCREASE_RATE * timepass), player=player)

    player.update()
    screen.blit(player.image, player.rect)
    player.image.set_colorkey((0, 0, 0))



## check for collisions between player and coins
    result = pygame.sprite.spritecollide(player, coins, True)
    if result:
        score += len(result)

    result = pygame.sprite.spritecollide(player, apples, True)
    if result:
        score += 10
        apple_effect_start_time = pygame.time.get_ticks()



    if apple_effect_start_time > 0:
        elapsed_time = pygame.time.get_ticks() - apple_effect_start_time
        if elapsed_time < apple_effect_duration:

            player.speed = player.speed_increase(1.05)
        else:
            apple_effect_start_time = 0
            player.speed = 10

    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        lives -= len(result)
        ouch.play()
        pygame.mixer.music.play(1)

        screen.blit(ouchimage, player.rect)
        pygame.display.flip()

        pygame.time.delay(1000)
        add_enemies(1)



    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)



    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    apples.draw(screen)
    coins.draw(screen)
    enemies.draw(screen)
    player.draw(screen)

    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    pygame.display.update()

pygame.mixer.music.stop()

closingmenumusic = pygame.mixer.music.load("../FinalProject/Assets/sounds/wompwomp.mp3")
closingmenu(screen, closingmenumusic, score)

player.update()
save_highscore(score)
pygame.mixer.music.stop()
pygame.quit()
sys.exit()




