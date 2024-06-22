class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def main(self):
        print("drive")

class Boat:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def main(self):
        print("sail")

class Aeroplane:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def main(self):
        print("fly")

# Creating instances of each class
V = Car("x7", "bmw")
B = Boat("cv100", "eicher")
M = Aeroplane("v900", "emirates")

# Looping through the instances and calling their main method
for i in (V, B, M):
    i.main()
