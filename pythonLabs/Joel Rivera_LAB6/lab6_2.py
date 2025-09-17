#lab6_2.py – Joel Rivera

#making a list of usernames
usernames=[]

#looping through the list
for name in usernames:
    if name=='ADMIN':
        print(f'Hello {name}, would you like to see a status report?')
    else :
        print(f'Hello {name}, thank you for logging in again!')

#empty list message
if usernames==[]:
    print(f'We need to find some users.')