#lab11_5.py – Joel Rivera

#define function createUser() with arbitrary parameter
def createUser(**dict):
    return dict

#define function printUser() with user parameter
def printUser(user):
    for key in user.keys():
        print(f'{key}: {user[key]}')

user1=createUser(name='John', age=43, job='Programmer', hobby='Biking')
user2=createUser(name='Sara', age=24, school='QCC', major='CSIS')
printUser(user1)
print()
printUser(user2)