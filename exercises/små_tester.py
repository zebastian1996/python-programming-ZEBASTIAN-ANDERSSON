#            oop  förälder class




class Djur:

    def __init__(self, name, animal):
        self.name = name 
        self.animal = animal

    def sleeping(self):
        print(f"{self.name} is sleeping")

    def eating(self):
        print(f"{self.name} is eating")

class hunter(Djur):

    def hunting(self):
        print(f"{self.name} the {self.animal} is hunting")

class pray(Djur):

    def hunted(self):
        print(f"{self.name} the {self.animal} is hunting")


cat = hunter("tom", "cat")
mouse = pray("jerry", "mouse")
tiger = hunter("simon", "tiger")
capibara = pray("alex", "antilop")


cat.sleeping()
mouse.hunted()
tiger.hunting()
capibara.hunted()
