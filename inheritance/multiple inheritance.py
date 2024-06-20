class parent1:
    def walk(self):
        print("he can walk!")
    def sing(self):
        print("he can sing!")
class parent2:
    def dance(self):
        print("he can dance!")
    def eat(self):
        print("he can eat")
class child(parent1,parent2):
    def party(self):
        print("he can party!")
d=child()
d.walk()
d.sing()
d.dance()
d.eat()
d.party()                             