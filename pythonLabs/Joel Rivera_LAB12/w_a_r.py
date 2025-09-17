#lab12_3.py – Joel Rivera

#defining a function that writes names
def wrte(fileN):
    presidents=['George Washington', 'John Adams', 'Thomas Jefferson']
    with open(fileN, 'w') as file:
        for pres in presidents:
            file.write(f'{pres}\n')

#defining a function that appends three more names
def app(fileN):
    presidentsTwo=['James Madison', 'James Monroe', 'John Q. Adams']
    with open(fileN, 'a') as file:
        for p in presidentsTwo:
            file.write(f'{p}\n')

#defining a function that reads and displays contents of created file
def rd(fileN):
    with open(fileN) as file:
        text = file.read()
        print(text, end='')