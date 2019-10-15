from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return ('Vector(%r %r)'%(self.x, self.y))
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(scalar*self.x, scalar*self.y)
    
vect = Vector(2,1)
vect1 = Vector(2,4)
print(vect+vect1)
print(abs(vect))
print(2*vect)