#lab2_2.py – Joel Rivera

#creating the variable
email='joel.rivera74@student.qcc.cuny.edu'

#using slicing to  print the entire email adress
print(email[:])

#using slicing and find() string methods to print user name
#using slicing, find() and rfind() string methods to print company name
i = email.find('@')
newEmail = email[i+1:]
j = newEmail.find('.')
k= newEmail.rfind('.')

print('User Name: ', email[:i].lower())
print('Company Name: ', newEmail[j+1:k].upper())
