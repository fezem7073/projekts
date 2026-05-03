import pygame
import time
import random

pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("llllooooooooooooooooooollllllllllllll")


bild = pygame.image.load('/home/lennard/Pictures/20250314_13h06m19s_grim.png')
bild = pygame.transform.scale(bild, (width, height))
screen.blit(bild, (0, 0))

#screen.fill("blue")

clock = pygame.time.Clock().tick(60)

spielaktiv = True


while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:                      #elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hat Taste gedrückt")
            if event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
            elif event.key == pygame.K_1:
                print("nein")





pygame.display.update()


