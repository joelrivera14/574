#lab8_5.py – Joel Rivera
import random

#defining message function to print p1, p2 times
def message(p1, p2):
    i = 0
    while i < p2:
        print(f'{p1}')
        i +=1

#defining main function
def main():
#requesting a text and printing
    text = input('Enter a text: ')
    print(f'text = {text}')
#generating a random number and printing
    n = random.randint(1,10)
    print(f'n = {n}\nmessage(text, n) will print the following:')
    message(text, n)
main()