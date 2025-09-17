#lab7_2.py – Joel Rivera

#using a for loop to print even && multiple of 3 numbers
for num in range(1,1000):
    if num % 2 ==0 and num % 3 == 0:
        print(f'{num}', end=' ')
print()

#converting to a while loop
#using a counter
i = 1
while i < 1000:
#incrementing counter with each iteration
    i+=1
    if i % 2 ==0 and i % 3 == 0:
        print(f'{i}', end=' ')
print()