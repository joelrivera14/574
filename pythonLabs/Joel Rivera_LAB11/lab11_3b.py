#lab11_3b.py – Joel Rivera

#using list comprehension to create a list of letters
alphabetTwo= [chr(a) for a in range(ord('a'), ord('z')+1)]

#using list comprehension to create a list of numbers
numTwo= [i for i in range(100, 2601, 100)]

#creating a dictionary of the merged lists
numChar= dict(zip(numTwo, alphabetTwo))

#using a for loop to print keys and values using items()
for key, value in numChar.items():
    print(f'{key} {value.upper()}', end='|')
print()

#using a for loop to append letters to an empty list
alphabet=[]
for letter in range(ord('a'), ord('z')+1):
    letters=chr(letter)
    alphabet.append(letters)

#using list comprehension to create a list with 26 numbers
num=[i for i in range(1,27)]

#creating a merged dictionary
charNum=dict(zip(alphabet,num))

#merging both dictionaries into one
all= {**charNum, **numChar}
print(f'{all}')