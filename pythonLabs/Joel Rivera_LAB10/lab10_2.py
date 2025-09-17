#lab10_2.py – Joel Rivera
from rectangle import Rectangle

#instantiate two objects of type rectangle
r1= Rectangle(4,5)
r2= Rectangle()

#calling display(), printing area()
r1.display()
print(f'Area: {r1.area()}')
r2.display()
print(f'Area: {r2.area()}')

#calling setWidth(), setHeight() and updating value
r2.setWidth(6)
r2.setHeight(6)

#displaying getWidth(), getHeight() with print
print(f'Get Width: {r2.getWidth()}')
print(f'Get Height: {r2.getHeight()}')

#printing area() of r2
print(f'Area: {r2.area()}')