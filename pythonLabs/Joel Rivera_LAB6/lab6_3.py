#lab6_3.py – Joel Rivera

#making a list of current users
current_users=['admin', 'tom', 'jerry', 'Dora', 'George']

#prompting username
userName=str(input('Enter your user name: ').lower())

#Print a message, Sorry that name is taken
#this if statment checks if userName is in
#lowercase names stemming from the original list current_users
if userName in (name.lower() for name in current_users):
    print(f'Sorry {userName}, that name is taken.\nCurrent users: {current_users}')
#if its a new name, append it
else:
    current_users.append(userName)
    print(f'Great, {userName} is still available\n{current_users}')