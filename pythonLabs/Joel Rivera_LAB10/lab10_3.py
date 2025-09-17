#lab10_3.py – Joel Rivera
from shapes import Rectangle, Circle

r1=Rectangle()
r1.display()
r1.setWidth(1.25)
r1.setHeight(1.25)
print(f'Get Width: {r1.getWidth()}')
print(f'Get Height: {r1.getHeight()}')
print(f'Area: {r1.area():.5f}')
print()

r2=Circle(0)
r2.display()
r2.setRadius(10)
print(f'Get Radius: {r2.getRadius()}')
print(f'Area: {r2.area():.5f}')
print(f'Circumference: {r2.circumference():.5f}')