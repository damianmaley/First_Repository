'''class: Circles
Class attributes: pi = 3.14
Intance attribute = radius
class methods: area, circumference
objects:circles1, circle2
'''
# ceil rounds up the output to a whole number 
from math import ceil
class Circles:
    #class attribute
    pi = 3.142

    #instantiation
    def __init__(self, radius):
        #instance attribute
        self.radius = radius
        
    # 2 * pi * radius
    def circumference(self):
        return ceil(2 * self.pi * self.radius)
    
    # pi * radius **2
    def area(self):
        return ceil(self.pi * self.radius **2)

circle1 = Circles(24)
circle2 = Circles(23)

print(circle1.circumference())
print(circle1.area())
print(circle2.circumference())
print(circle2.area())

print(circle1.pi)

