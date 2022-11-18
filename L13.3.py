class StringVar():
    def set(self,value):
        self.s=value
    def get(self):
        return self.s

stV=StringVar()
stV.set(input())
print(stV.get())