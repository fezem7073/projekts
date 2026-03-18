import random

spielfeld = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]

def spielfeld_ausgeben():
    print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3])
    print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6])
    print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9])
spielfeld_ausgeben()

def ki_zug():
    o = random.randint(1, 10)
    print(o)
    spielfeld.insert(o, "O")

def spieler_zug():
    while True:
        x = input("Bitte Feld eingeben:")
        try:
            spielzug = int(x)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")

#while True:

spieler_zug()
ki_zug()
spielfeld_ausgeben()