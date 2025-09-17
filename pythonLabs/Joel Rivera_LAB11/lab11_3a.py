#lab11_3a.py – Joel Rivera

#using a for loop to append letters to an empty list
alphabet=[]
for letter in range(ord('a'), ord('z')+1):
    letters=chr(letter)
    alphabet.append(letters)

#using list comprehension to create a list with 26 numbers
num=[i for i in range(1,27)]

#creating a merged dictionary
charNum=dict(zip(alphabet,num))

#using a for loop to print keys and values using keys()
for key in charNum.keys():
    print(f'{key} {charNum[key]}', end='|')
print()