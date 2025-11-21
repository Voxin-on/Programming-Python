import math

class Vectors():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def lenVector(self):
        return (self.x**2+self.y**2)**(1/2)
    def angle(self):
        return math.degrees(math.atan2(self.y,self.x))
    def sumVector(self,otherVector):
        return (self.x+otherVector.x,self.y+otherVector.y)
    def minusVector(self,otherVector):
        return (self.x-otherVector.x,self.y-otherVector.y)
    def multVector(self, otherVector):
        return self.x * otherVector.x +self.y * otherVector.y

vector1=Vectors(4,3)
vector2=Vectors(2,2)
print(vector1.lenVector())
print(vector2.angle())
print(vector1.sumVector(vector2))
print(vector1.minusVector(vector2))
print(vector1.multVector(vector2))