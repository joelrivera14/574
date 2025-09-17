#lab5_2.py – Joel Rivera

#using list comprehension to generate a list of even numbers
even=[n for n in range(101) if n%2==0]
print(even)

#use slicing to print the first 5 numbers
print(even[:5])

#use slicing to print the last 5 numbers
print(even[-5:])

#use slicing and index to print 44-88
start, end= even.index(44), even.index(88)+1
print(even[start:end])