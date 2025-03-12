#lab9_5.py – Joel Rivera
from random import *

#define average() with a parameter that accepts an arbitrary number of values
def average(*grades):
#calculating average and then returning it
    aver=sum(grades)/len(grades)
    return aver

#define main()
def main():
#calling average()
    print(f'Average of 95, 87, 83, 74: {average(95, 87, 83, 74):.2f}')
#creating random integers
    x,y,z=randint(-100, -1), randint(0, 1), randint(1, 100)
    print(f'Average of any three random numbers, {x} {y} {z}: {average(x, y, z):.2f}')

main()
