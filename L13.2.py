class Animal():
    name=""

    def eat(self):
        print("Намнем!")
    def __init__(self, newName):
        self.name=newName
        print("Родилось новое животное!")
    def setName(self,newName):
        self.name=newName
    def getName(self):
        return self.name
    def makeNoise(self):
        print(self.name, "говорит Гррррррря")

myAnimal=Animal("Собака")
print(myAnimal.getName())
myAnimal.setName("Suren")
myAnimal.makeNoise()
myAnimal.eat()




