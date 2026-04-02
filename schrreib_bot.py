import random
import pyautogui as pg
import time

tiere = ["Hund", "Affe", "Esel"]

time.sleep(5)


for i in range (20):
    a = random.choice(tiere)
    pg.write(f"Du {a}")
    #time.sleep(1)
    pg.press("enter")