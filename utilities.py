import pygame
import sys
import random
from game_parameters import *
from enemy import Enemy, enemies
import pygame.mixer
import math



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


def add_enemies(num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2),
                          random.randint(SCREEN_HEIGHT //2, SCREEN_HEIGHT - 150)))

def mainmenu(screen, menumusic):
    menfont = pygame.font.Font("../FinalProject/Assets/fonts/BUMBASTIKA.TTF", 40)
    titlemessage = menfont.render("Hopper Run", True, (255,255,255))
    startmessage = menfont.render("Click SPACE to start", True, (255,255,0))
    backgr = (pygame.transform.scale(pygame.image.load("../FinalProject/assets/hopperhall.png"),
                                   (SCREEN_WIDTH, SCREEN_HEIGHT)).convert())
    screen.blit(backgr, (0, 0))
    pygame.mixer.music.play(-1)

    runningmen = True
    while runningmen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return


        screen.blit(titlemessage, (SCREEN_WIDTH / 2 - titlemessage.get_width() / 2, SCREEN_HEIGHT / 3))
        screen.blit(startmessage, (SCREEN_WIDTH / 2 - startmessage.get_width() / 2, SCREEN_HEIGHT / 2))

        pygame.display.update()

def cutscene(screen):

    backimage = (pygame.transform.scale(pygame.image.load("../FinalProject/assets/backgroundtest.png"),
                                   (SCREEN_WIDTH, SCREEN_HEIGHT)).convert())
    screen.blit(backimage, (0, 0))
    cutplayer = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/cutscenetest.png"),(550,650)).convert()
    cutplayer.set_colorkey((0, 0, 0))

    player_x = SCREEN_WIDTH - (SCREEN_WIDTH - 50)
    player_y = (SCREEN_HEIGHT) // 2

    screen.blit(cutplayer, (player_x, player_y))

    susmusic = pygame.mixer.music.load("../FinalProject/Assets/sounds/dundundun.mp3")

    runningmen = True
    while runningmen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return






        pygame.display.update()

def cutscene2(screen, susmusic):

    backimage = (pygame.transform.scale(pygame.image.load("../FinalProject/assets/backgroundtest.png"),
                                   (SCREEN_WIDTH, SCREEN_HEIGHT)).convert())
    screen.blit(backimage, (0, 0))
    cutenemy = pygame.transform.scale(pygame.image.load("../FinalProject/Assets/cutscene2test.png"),(500,500)).convert()
    cutenemy.set_colorkey((0, 0, 0))

    player_x = SCREEN_WIDTH - 450
    player_y = (SCREEN_HEIGHT) // 2

    screen.blit(cutenemy, (player_x, player_y))
    pygame.mixer.music.play(-1)
    runningmen = True
    while runningmen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return






        pygame.display.update()
def closingmenu(screen, closingmenumusic, score):

    highscore = load_highscore()
    save_highscore(score)

    menfont = pygame.font.Font("../FinalProject/Assets/fonts/JungleAdventurer.ttf", 50)
    titlemessage = menfont.render("Game is over :(((  BUT SO IS THE SEMESTER!!!! WOOHOOOOOO", True, (255,255,0))
    score_text = menfont.render(f"Score: {score}    High score: {highscore}", True, (255, 255, 0))



    pygame.mixer.music.play(3000)

    runningmen = True
    while runningmen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        screen.fill((128, 0, 128))
        screen.blit(titlemessage, (SCREEN_WIDTH / 2 - titlemessage.get_width() / 2, SCREEN_HEIGHT / 3))
        screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, SCREEN_HEIGHT / 2))


        pygame.display.flip()

def save_highscore(score):
    try:
        with open("high_score.txt", "r") as file:
            content = file.read().strip()
            if content:
                current_high_score = int(content)
            else:
                current_high_score = 0
    except FileNotFoundError:
        current_high_score = 0

    if score > current_high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(score))


def load_highscore():
    try:
        with open("high_score.txt", "r") as file:
            content = file.read().strip()
            if content:
                return int(content)
            else:
                return 0
    except FileNotFoundError:
        return 0