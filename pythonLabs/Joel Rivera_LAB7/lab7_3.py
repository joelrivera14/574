#lab7_3.py - Joel Rivera

#using a for loop to calculate the sum of 1-100
total= []
for num in range(1,101):
    total.append(num)
print(f'Sum = {sum(total)}')

#using a while loop for the sum of all even
total=[]
i=1
while i <101:
#checking if even
    if i % 2 == 0:
        total.append(i)
    i+=1
print(f'Sum = {sum(total)}')