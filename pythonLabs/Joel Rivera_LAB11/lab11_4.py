#lab11_4.py – Joel Rivera

#create 3 dictionaries
stuInfo1={'name':'tom cat', 'gpa':3.456}
stuInfo2={'name':'jerry mouse', 'gpa':4.0}
stuInfo3={'name':'sponge bob', 'gpa':3.99}


#Create a list and add all dictionaries
stuClass=[stuInfo1, stuInfo2, stuInfo3]
print(f'All students in the list:\n{stuClass}')
print()

#Use a loop to print all students list 
print(f'All students information:')
count = 1
for student in stuClass:
    print(f'Student {count} {student}')
    count +=1
print()

#use a loop to print all gpa
print(f'All gpa information:')
for student in stuClass:
    print(f'{student['gpa']}', end='|')
print()
print()

#Changing the last student’s gpa to 4.0, adding a new student info to the list.
stuInfo3['gpa']=4.0
stuInfo4={'name':'john smith', 'gpa':3.99}
stuClass.append(stuInfo4)

#Use a loop to print all names and gpa, using string formatting to line up output
print(f'All the updated information:')
for student in stuClass:
    print(f"{student['name'].title():<20}{student['gpa']:>1.2f}")