#lab10_3.py - Joel Rivera
from math import pi

#implement class rectangle
class Rectangle:
    #implement init method with optional parameter type
    def __init__(self, width=1, height=1, type=None):
        self.width= width
        self.height= height
        self.type= type

    #implement display()
    def display(self):
        print(f'Width: {self.width}\nHeight: {self.height}')
    
    #implement setwidth() to assign width to the instance variable
    def setWidth(self, width):
        self.width= width
    
    #implement setheight() to assign width to the instance variable
    def setHeight(self, height):
        self.height= height 
    
    #implement getWidth() to return value instance variable width
    def getWidth(self):
        return self.width
    
    #implement getHeight() to return value instance variable height
    def getHeight(self):
        return self.height
    
    #implement area() to return value of area of rectangle
    def area(self):
        return self.width * self.height


#implement cicle class
class Circle:
    #implment __init__() with radius and optional parameter type
    def __init__(self, radius=1, type=None):
        self.radius= radius
        self.type= type

    #implement display() to print value of radius
    def display(self):
        print(f'Radius: {self.radius}')
    
    #Implement setRadius() to assign radius to the instance variable
    def setRadius(self, radius):
        self.radius= radius
    
    #Implement getRadius()to return the value of instance variable radius
    def getRadius(self):
        return self.radius
    
    #Implement area() to return the value of area of a circle
    def area(self):
        return pi * self.radius**2
    
    #Implement circumference(), return circumference of a circle.
    def circumference(self):
        return 2 * pi * self.radius