#lab5_1.py – Joel Rivera

#A: Print all the odd numbers from 1 to 9 inclusive in a list, odd_num.
odd_num=[]
for num in range(10):
    if (num%2!=0):
        odd_num.append(num)
print(odd_num)

#B: Make a list of the first 10 cubes.
#Use a for loop to print out the value of each cube in a new line (see output below).
for num in range(11):
    print(num**3)

#C: Use a list comprehension to generate a list of the first 10 cubes.
#Use a for loop to print out the value of each cube in a row separated by a ‘|’ (see output below).
firstTen=[num**3 for num in range(11)]

for num in firstTen:
    print(f'{num}', end='|')