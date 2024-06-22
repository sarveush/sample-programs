class Car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def main(self):
        print("on road!")
class Boat(Car):
    def main(self):
        print("on sea!")
class Aeroplane(Car) :
    def main(self):
        print("on Sky!")
p=Car("bmw","x7")
o=Boat("eicher","v460")
y= Aeroplane("Emiates","h980")
for x in (p,o,y):
    print(x.model)
    print(x.brand)
    x.move()           
        