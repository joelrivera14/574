#lab5_2.py – Joel Rivera

#using list comprehension to generate a list of even numbers
evenNums=[num for num in range(101) if num%2==0]

#use slicing to print the first 5 numbers
print(f'{evenNums[0:5]}')

#use slicing to print the last 5 numbers
print(f'{evenNums[-5:]}')

#use slicing and index to print 44-88
start, end=evenNums.index(44), evenNums.index(88)+1
print(f'{evenNums[start:end]}')