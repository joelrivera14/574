#lab7_1.py – Joel Rivera

#requesting an interger input
#using exception handling
try:
    number = int(input("Enter an integer number, and I'll tell you if it's a multiple of ten: "))
#checking if its a multiple of ten
    if number % 10 == 0:
        print(f'{number} is a multiple of ten.')
    else:
        print(f'{number} is not a multiple of ten')
except:
    print(f'Invalid input.')