#lab7_6.py - Joel Rivera

#requesting two numbers from console
nOne = int(input('Enter a number n1: '))
nTwo = int(input('Enter a number n2: '))

#use a while loop to print if n1 < n2
if nOne < nTwo:
    while nOne < nTwo+1:
        print(f'{nOne}', end='|')
        nOne += 1

#using a for loop to print if n1 > n2
elif nOne > nTwo:
    for num in range(nOne, nTwo-1, -1):
        print(f'{num}', end='|')

#if equal
else:
    print(f'n1 = n2')
print()