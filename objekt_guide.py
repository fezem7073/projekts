class Person:
    def __init__(self, name, age, g): # __init__ ist der Konstruktor, self ist die neue Instanz
        self.name = name         # self.name ist ein Attribut dieser spezifischen Instanz
        self.age = age
        self.g = g
        print(f"name={g}")# self.age ist ebenfalls ein Attribut dieser Instanz

    def greet(self):             # greet ist eine Methode, die 'self' benötigt
        return f"Hallo, mein Name ist {self.name}." # Zugriff auf self.name
    
    def celebrate_birthday(self): # Methode, die den Zustand der Instanz ändert
        self.age += 1
        print(f"Happy Birthday! {self.name} ist jetzt {self.age} Jahre alt. ist {self.g} groß")

# Instanz erstellen
p1 = Person("Anna", 30, 160)
p2 = Person("Max", 25, 130)
print(Person("kei", 90, 300).greet())

# Methoden aufrufen
print(p1.greet()) # Gibt "Hallo, mein Name ist Anna." aus
print(p2.greet()) # Gibt "Hallo, mein Name ist Max." aus

print(p1.name)
p1.name = "jannis"
print(p2.age)
print(p1.name)
 
p1.celebrate_birthday()
p2.celebrate_birthday()# Gibt "Happy Birthday! Anna ist jetzt 31 Jahre alt." aus