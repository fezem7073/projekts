import pygame
import time
import random

# pygame
pygame.init()
pygame.display.set_caption("RPG")

#                   Variablen                  #


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


#Player
player_x = 600
player_y = 100
player_sice = 50
player_color = ROT

player_alt_x = player_x
player_alt_y = player_y
player_alt_sice = player_sice

#Game cycle

clock = pygame.time.Clock().tick(60)
gameactive = True


#Karte

boden = pygame.draw.rect(screen, GRUEN, [500, 400, 500, 50])


#               Funktionen              #

def player_löschen(x, y):
    pygame.draw.circle(screen, SCHWARZ, (x, y), player_sice)



while gameactive:

    for event in pygame.event.get():

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gameactive = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #player_x -= 
                print("a")
            elif event.key == pygame.K_RIGHT:
                #player_x += 
                print("d")
            #elif event.key == pygame.K_SPACE:




    player_alt_x = player_x
    player_alt_y = player_y


    #               Draw                #
    player_löschen(player_alt_x, player_alt_y)    
    player = pygame.draw.circle(screen, player_color, (player_x, player_y), player_sice)
    


    pygame.midi


#                   Game Logic                  #

    #gravitation
    player_y += 1


    if player.colliderect(boden):
        player_y -= 1


    pygame.display.flip()

#pygame.display.update()

pygame.quit()