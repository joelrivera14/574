#lab4_3.py – Joel Rivera

#creating a list called courses
courses=['MA-121','ET-506', 'ET-704', 'ET-574', 'HIST-110']
print(f'{courses}')

#using the len() method to print my courses
print(f'I am taking {len(courses)} courses.')

#using indexing to print 1st and last items
print(f'{courses[0]}\t{courses[-1]}')

#using slicing to print classes
print(f'{courses[:4]}')
print(f'{courses[-4:]}')
print(f'{courses[1:4]}')