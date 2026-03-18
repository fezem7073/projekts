import random

class bluebrint_auto():
    """Klasse für Autos"""

    def __init__(self, model:str, farbe: str, kmstand: int = 0, alter = 0):
        self.model = model
        self.farbe = farbe
        self.kmstand = kmstand
        self.alter = alter
        pass

    def auto_fahren(self, länge):
        print(f"{self} ist {self.kmstand}km Gefahren")
        self.kmstand += länge
        print(f"{self} ist hat jetzt einen km stand von: {self.kmstand}")

class mini(bluebrint_auto):
    
    def __init__(self, model:str, farbe, kmstand = 0, alter=0):
        super().__init__(model, farbe, kmstand, alter)
    
    def mini_sachen(self, sache: str):
        print(f"{self} macht {sache}")