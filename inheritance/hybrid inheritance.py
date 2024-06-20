class Grandfather:
    def walk(self):
        print("he is walkinhg!")
class Grandmother:
    def sing(self):
        print("she is singing!")
class mother:
    def cook(self):
        print("she is cooking!")
class father(Grandfather,Grandmother):
    def work(self):
        print("he is working!")
class son(father):
    def play(self):
        print("he is playing!")   
d=son()
d.walk()
d.sing()
d.work()
d.play()  

# mother
c=mother()
c.cook()
