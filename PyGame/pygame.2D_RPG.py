import pygame
import time
import random

# pygame
pygame.init()
pygame.display.set_caption("RPG")

#                   Variablen                  #


def multi(zahl):
    zahl *= multiplikator
    return zahl

#Pygame Screen

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height))

#Farben

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

#Karte

karte = [
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1],
]



#game logic
multiplikator = 80

#Player
player_x = multi(5.5)
player_y = multi(7.5)
player_sice = multi(0.5)
player_color = ROT

player_alt_x = 0
player_alt_y = 0
player_alt_sice = 0

#Wall
wall_color = ORANGE


#Game cycle

clock = pygame.time.Clock().tick(60)
gameactive = True

#               Funktionen              #


def draw_wall(x, y):
    global wall
    wall = pygame.draw.rect(screen, wall_color, [multi(x), multi(y), multi(1), multi(1)])

def delet_player(x, y):
    pygame.draw.circle(screen, SCHWARZ, (x, y), multi(0.5))



#       Karte vorbereiten       #

for x in range(0, 20):
    for y in range(0, 7):
        if karte[y][x] != 0:
            draw_wall(x, y)


#                      Gameloop                     #

while gameactive:

    for event in pygame.event.get():

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gameactive = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:               
                player_y -= multi(1)
                print("w")
            elif event.key == pygame.K_s:               
                player_y += multi(1)
                print("s")
            elif event.key == pygame.K_a:                
                player_x -= multi(1)
                print("a")
            elif event.key == pygame.K_d:                              
                player_x += multi(1) 
                print("d")





    #               Draw                #

    player = pygame.draw.circle(screen, player_color, (player_alt_x, player_alt_y), player_sice)


#                   Game Logic                  #








    pygame.display.flip()

pygame.display.update()

pygame.quit()