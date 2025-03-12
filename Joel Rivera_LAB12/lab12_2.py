#lab12_2.py – Joel Rivera

#creating a function to create a file
def presidentTwo(filename):
    presidents = [
        'George Washington', 'John Adams'
    ]
# opening the file in write mode, if the file exist it is overwritten and if it
# doesnt exist, a new file will be created 
    with open(filename) as file:
#iterating through the list to write each item individually
        for president in presidents:
#file.write writes the data directly to the file
            file.write(f'{president}\n')

def presidentThree(fileN):
    pres= [
        'George Washington', 'John Adams', 'Thomas Jefferson'
    ]
    with open(fileN) as file:
        for p in pres:
            file.write(f'{p}\n')

presidentTwo('Presidents2.txt')
presidentThree('Presidents3.txt')