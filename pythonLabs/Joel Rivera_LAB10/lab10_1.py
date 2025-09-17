#lab10_1.py – Joel Rivera

#implementing the class
class Rectangle:
    #defining and init method
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    #implementing display method
    def display(self):
        print(f'Width: {self.width}\nHeight: {self.height}')

#instantiate two objects of type rectangle
r1 = Rectangle(4,5)
r2 = Rectangle(10,10)

#call display
r1.display()
r2.display()

print(f'Width of r1: {r1.width}\nHeight of r2: {r2.height}')