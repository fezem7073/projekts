import pygame
from pygame.locals import *



pygame.init()




# Variablen/KONSTANTEN setzen

W, H = 800, 600
FPS  = 60
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
GRAU    = ( 155, 155, 155)

spielaktiv = True

# Definieren und Öffnen eines neuen screens

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Grafiken nutzen")
clock = pygame.time.Clock()

player = pygame.image.load("/home/lennard/Pictures/biene.png")

player_größe = player.get_rect()

print(player_größe)
print(player_größe.centerx)
print(player_größe.centery)
print(player_größe.width)
print(player_größe.height)








# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        # Beenden bei [ESC] oder [X]
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            spielaktiv = False

    # Spiellogik

    # Spielfeld löschen
    screen.fill(GRAU)

    # Spielfeld/figuren zeichnen

    screen.blit(player, (5, 5))

    screen.blit(pygame.transform.rotate(player, 90), (50, 50))


    # screen aktualisieren
    pygame.display.flip()
    clock.tick(FPS)