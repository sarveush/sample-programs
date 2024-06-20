class parent:
    def walk(self):
        print("he is walkinh!")
    def sing(self):
        print("he is singing!")
class child(parent):
    def dance(self):
        print("he is dancing!")
p=child()
p.walk()
p.sing()
p.dance()                   

