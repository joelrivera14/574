#lab4_1.py – Joel Rivera

#create an empty list
n=[]

#adding to the list
n.append(2)
n.append(4)
print(n)

n.insert(0,0)
n.insert(1,1)
n.insert(3,3)
print(n)

n.append(5)
print(n)

#removing from the list
n.pop(0)
print(n)

#storing the pop() value in a variable
x=n.pop(1)
print(f'{n} \n{x}')

y=n.pop(2)
print(f'{n} \n{y}')

#sum of removed numbers
sum=x+y
print(f'Sum of all removed numbers = {sum}')

#changing the first and last numbers
n.pop(0)
n.pop(1)
n.insert(0,100)
n.append(9.9)
print(n)

#copying the list
newNum=list(n)
n.clear()
print(f'Original list = {n} \nNew list = {newNum}')

#delete the n list
del n