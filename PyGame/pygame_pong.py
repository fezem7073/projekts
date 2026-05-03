import pygame
import time
import random

# pygame
pygame.init()
pygame.display.set_caption("Ping Pong Spiel")

# Variablen
spielaktiv = True
clock = pygame.time.Clock()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 62
screen = pygame.display.set_mode((width, height))

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

ball_move_tick_x = 4
ball_move_tick_y = 4
ball_pos_x = 810
ball_pos_y = 500
ball_größe = 20

spieler1_pos_Y = 20
spieler1_move_Y = 75

spieler2_pos_Y = 20
spieler2_move_Y = 75

score = 0

print(f"h=" + str(height))
print(f"w=" + str(width))

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                spieler1_pos_Y -= spieler1_move_Y
                print("w")
            elif event.key == pygame.K_s:
                spieler1_pos_Y += spieler1_move_Y
                print("s")
            elif event.key == pygame.K_UP:
                spieler2_pos_Y -= spieler2_move_Y
                print("^")
            elif event.key == pygame.K_DOWN:
                spieler2_pos_Y += spieler2_move_Y
                print("v")


    # Spielfeld löschen
    screen.fill(SCHWARZ)

    # Spielfeld/figuren zeichnen
    ball = pygame.draw.ellipse(screen, WEISS, [ball_pos_x,ball_pos_y,ball_größe,ball_größe])
    spieler1 = pygame.draw.rect(screen, ROT, [20, spieler1_pos_Y, 20, 100])
    spieler2 = pygame.draw.rect(screen, ROT, [1880, spieler2_pos_Y, 20, 100])


    # Spiellogik hier integrieren
    ball_pos_x += ball_move_tick_x
    ball_pos_y += ball_move_tick_y

    if ball_pos_y > height - ball_größe or ball_pos_y < 0:
        ball_move_tick_y = ball_move_tick_y * -1
    elif ball_pos_x > width - ball_größe or ball_pos_x < 0:
        ball_move_tick_x = ball_move_tick_x * -1


    if spieler1.colliderect(ball):
        ball_move_tick_x = ball_move_tick_x * -1
        ball_pos_x = 40
        score += 1
    if spieler2.colliderect(ball):
        ball_move_tick_x = ball_move_tick_x * -1
        ball_pos_x = 1860
        score += 1


    ausgabetext = "Score: " + str(score)
    font = pygame.font.SysFont(None, 70)
    text = font.render(ausgabetext, True, ROT)
    screen.blit(text, [800, 10])

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()