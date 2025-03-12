#lab11_1.py – Joel Rivera

#creating dictionary
stuInfo={'name':'John Smith', 'gpa':3.456, 'age':20}
#print(stuInfo['name']), how i understand line 15, output is the value of key

#printing all keys and values with a loop
for key, value in stuInfo.items():
    print(f'{key.upper()}\t{value}')
print()

#using the update() method and printing all keys, values with keys()
stuInfo.update({'gpa':4.0})
for key in stuInfo.keys():
    print(f'{key.upper()}\t{stuInfo[key]}')
print()

#adding a key major and printing all values with using a loop
stuInfo['major']='CSIS'
for val in stuInfo.values():
    print(f'{val}', end="|")
print()
print()

#two ways to delete gpa, age and printing updated dictionary
del stuInfo['gpa']
stuInfo.pop('age')

print(f'{stuInfo}')