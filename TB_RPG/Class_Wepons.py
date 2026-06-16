class weapons():#

    global equiped_weapon

    def __init__(self, name:str, damage:int, weight:int, durability:int=100):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.durability = durability

    def equip(self):
        globle equiped_weapon
        
        equiped_weapon = self.name  ####################
        print(f"You have equipped {self.name}.")
    def unequip(self):
        self.equipped = False
        print(f"You have unequipped {self.name}.")
    def attack(self):
        if self.equipped:
            print(f"You attack with {self.name} for {self.damage} damage.")
            return self.damage
        else:
            print("You are not equipped with a weapon.")
