class Animal():
    name=""
    def __init__(self):
        print("Родилась анималя")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Родился кат!")
    def makeNoise(self,newName):
        self.name=newName
        print(self.name, "говорит мяу!")
    def eat(self):
        print("Вы кинули рыбу и", self.name, "ее схавал!")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Родилась дога!")
    def makeNoise(self,newName):
        self.name=newName
        print(self.name, "не говорит, молчит...")
    def eat(self):
        print("Вы кинули гречу и",self.name,"ее схавала!")

myCat=Cat()
myCat.makeNoise("Кат")
myCat.eat()
myDog=Dog()
myDog.makeNoise("Дога")
myDog.eat()