class Grandfather:
    def walk(self):
        print("he can walk")
class father(Grandfather):
    def eat(self):
        print("he can eat!")
class child(father):
    def party(self):
        print("he can party!")
d=child()
d.walk()
d.eat()
d.party()                        