#lab6_4.py – Joel Rivera

#creating new list called vehicles 
vehicles = ['car', 'Truck', 'boat', 'PLANE']

#Prompting input for a search letter
letter = str(input('Enter a search letter: ')).lower()

#checking if the length of letter is more than 1
if len(letter) != 1:
    print(f'Invalid search letter')

# Use the decision structure in a for loop to search all the items
else:
    for name in vehicles:
        #if the letter is in each string
        if letter in name.lower():
            #storing the index in a variable
            i=name.lower().index(letter)
            print(f"{name} contains '{letter}' and it is in position {i}")
        else:
            print(f"{name} does not contain '{letter}'")


