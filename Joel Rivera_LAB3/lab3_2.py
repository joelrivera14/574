#lab3_2.py - Joel Rivera

#prompt and request an input string from the console
prompt = input('Please enter a string: ')

#displaying the output
print('Original Text:', prompt,'\n', 'First Letter:', prompt[0],'\n', 'Last Letter:', prompt[-1],'\n', 'Reversed Text:', prompt[::-1], sep='')