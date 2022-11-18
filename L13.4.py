class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def plus(self):
        return(self.x+self.y)

q=Point(2,6)
print(q.plus())

