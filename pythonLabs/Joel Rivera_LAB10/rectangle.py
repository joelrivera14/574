#lab10_2.py – Joel Rivera

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