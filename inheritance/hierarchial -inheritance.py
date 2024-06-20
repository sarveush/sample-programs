class father:
    def walk(self):
        print("he is walking!")
class son1(father):
    def eat(self):
        print("he is eating!")
class son2(father):
    def sleep(self):
        print("he is sleeping!")
class child1(son1):
    def play(self):
        print("he is playing!")
class child2(son1):
    def cook(self):
        print("he is cooking!")
d=child1()
d.walk()
d.eat()
d.play()
d.cook()
  
