#lab5_4.py – Joel Rivera

#using for loop with input
try:
    #prompting integer range
    numRange=int(input('Enter a range: '))

#implementing a list of numbers from 1 to range inclusive
    newList=list(range(1, numRange+1))

#prompting integer number
    newNum=int(input('Enter an integer number: '))

#using a for loop to print multiplication table of number
    print(f'Multiplication table of {newNum}')
    for num in newList:
        print(f'{num}\tX\t{newNum}\t=\t{num*newNum}')
except:
    print(f'Invalid Input.')