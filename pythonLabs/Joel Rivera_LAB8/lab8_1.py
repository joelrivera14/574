#lab8_1.py – Joel Rivera
from math import fmod, ceil

try:
#prompting for two numbers
    num1 = int(input('Enter a numerator: '))
    num2 = int(input('Enter a denominator: '))

#using a sentinel-controlled loop
    while num2 == 0:
        print(f'Denominator can not be zero. Try again.')
        num2 = int(input('Enter a denominator: '))
    
    #using fmod() and printing result as an int
    print(f'{num1} mod {num2} = {ceil(fmod(num1,num2))}')

except:
    print(f'Invalid Input')