import pygame
from pygame.locals import *
import time
import random

pygame.init()
pygame.display.set_caption("Vorlage")




#                   Variablen                  #



#Farben
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)


#Pygame Screen
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
#screen = pygame.display.set_mode((width, height))

W, H = 800, 600
FPS  = 60
fenster = pygame.display.set_mode((W, H))

#game
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while True:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        # Beenden bei [ESC] oder [X]
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()

    # Spiellogik



    # Spielfeld löschen
    fenster.fill(WEISS)




    # Spielfeld/figuren zeichnen





    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)