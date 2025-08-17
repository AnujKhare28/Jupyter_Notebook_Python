import math
class Shape: 
    def __init__(self, name):
        self.name = name

    def area(self): 
        pass

class Rectangle(Shape):
    def __init__(self, len, bre):
        self.len = len
        self.bre = bre
        
    def area(self):
        return self.len * self.bre
    
class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return math.pi * (self.rad ** 2)
    
rect = Rectangle(10,5)
circ = Circle(7)
print("Area of rectangle:", rect.area())
print("Area of circle:", round(circ.area(), 2))